// build_speech_docx.js
//
// Usage:
//   node build_speech_docx.js <input.json> <output.docx>
//
// Input JSON schema:
// {
//   "event": "Lễ Tổng Kết 2026",
//   "subtitle": "Công bố Định hướng AI Powered School",
//   "speaker_name": "Ms Nguyễn Thuỳ Anh",
//   "speaker_role": "Viện trưởng — Major Education",
//   "language": "vi",                           // "vi" or "en"
//   "include_original": true,                   // whether to render Part I
//   "original": [                                // array of strings, each = 1 paragraph; bullet items start with "- "
//     "Xin kính chào Quý Phụ huynh,",
//     "- Nỗ lực của thầy cô...",
//     ...
//   ],
//   "upgraded": [                                // array of section objects
//     {
//       "timestamp": "[00:00–00:45]",
//       "title": "HOOK — Đặt câu hỏi định mệnh",
//       "stage_notes": ["Bước ra, im lặng 4 giây, nhìn khán phòng."],
//       "paragraphs": [
//         "Năm 2007, một chiếc điện thoại ra đời...",
//         { "type": "highlight", "text": "Câu in đậm key" },
//         { "type": "quote",     "text": "Câu quote đặc biệt mang màu xanh đậm" }
//       ]
//     },
//     ...
//   ],
//   "stage_directions": [                       // Part III — director notes
//     {"title": "Six stage moments", "bullets": ["...", "..."]},
//     {"title": "CTA mechanic", "bullets": ["...", "..."]}
//   ],
//   "comparison": [                             // table rows for old vs new
//     ["Tiêu chí", "Bản gốc", "Bản nâng cấp"],
//     ["Độ dài", "12–15 phút", "8–10 phút"],
//     ...
//   ],
//   "speakers_referenced": ["Steve Jobs", "JFK", "Oprah Winfrey"]
// }

const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error("Usage: node build_speech_docx.js <input.json> <output.docx>");
  process.exit(1);
}
const inputPath = args[0];
const outputPath = args[1];

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat,
  HeadingLevel, WidthType, ShadingType, PageNumber, PageBreak
} = require("docx");

const data = JSON.parse(fs.readFileSync(inputPath, "utf-8"));

// ===== helpers =====
const p = (text, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 120, before: opts.before ?? 0, line: opts.line ?? 320 },
  alignment: opts.align ?? AlignmentType.JUSTIFIED,
  children: [new TextRun({ text, bold: opts.bold, italics: opts.italics, size: opts.size ?? 24, color: opts.color })]
});

const ps = (runs, opts = {}) => new Paragraph({
  spacing: { after: opts.after ?? 120, before: opts.before ?? 0, line: opts.line ?? 320 },
  alignment: opts.align ?? AlignmentType.JUSTIFIED,
  children: runs
});

const t = (text, opts = {}) => new TextRun({
  text, bold: opts.bold, italics: opts.italics, size: opts.size ?? 24, color: opts.color
});

const h1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 360, after: 200 },
  children: [new TextRun({ text, bold: true, size: 36, color: "1F3864" })]
});

const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 280, after: 160 },
  children: [new TextRun({ text, bold: true, size: 28, color: "2E75B6" })]
});

const stageNote = (text) => new Paragraph({
  spacing: { before: 80, after: 80, line: 280 },
  alignment: AlignmentType.LEFT,
  children: [
    new TextRun({ text: "▸ Sân khấu: ", bold: true, italics: true, size: 20, color: "C00000" }),
    new TextRun({ text, italics: true, size: 20, color: "595959" })
  ]
});

const bullet = (text) => new Paragraph({
  numbering: { reference: "bullets", level: 0 },
  spacing: { after: 80, line: 300 },
  children: [new TextRun({ text, size: 24 })]
});

const blank = () => new Paragraph({ children: [new TextRun({ text: "" })] });

// Render a paragraph entry — can be string, or object with type
function renderParagraph(entry) {
  if (typeof entry === "string") {
    if (entry.startsWith("- ")) return bullet(entry.slice(2));
    return p(entry);
  }
  if (entry.type === "highlight") {
    return ps([t(entry.text, { bold: true })]);
  }
  if (entry.type === "quote") {
    return ps([t(entry.text, { bold: true, italics: true, color: "1F3864" })]);
  }
  if (entry.type === "mixed") {
    // array of {text, bold?, italics?, color?}
    return ps(entry.runs.map(r => t(r.text, r)));
  }
  return p(entry.text || JSON.stringify(entry));
}

// ===== Cover page =====
const cover = [
  new Paragraph({
    spacing: { before: 2400, after: 200 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: data.event || "BÀI PHÁT BIỂU", bold: true, size: 32, color: "1F3864" })]
  }),
  new Paragraph({
    spacing: { after: 600 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: data.subtitle || "", italics: true, size: 24, color: "2E75B6" })]
  }),
  new Paragraph({
    spacing: { after: 200 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: data.language === "en" ? "SPEECH SCRIPT" : "BÀI PHÁT BIỂU TRÊN SÂN KHẤU", bold: true, size: 28 })]
  }),
  new Paragraph({
    spacing: { after: 1200 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: data.language === "en" ? "Original + Upgraded version" : "Bản gốc + Bản nâng cấp song song", size: 22, color: "595959" })]
  }),
  new Paragraph({
    spacing: { after: 120 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: (data.language === "en" ? "Speaker: " : "Người trình bày: ") + (data.speaker_name || ""), size: 24 })]
  }),
  new Paragraph({
    spacing: { after: 600 },
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: data.speaker_role || "", italics: true, size: 22, color: "595959" })]
  }),
  data.speakers_referenced && data.speakers_referenced.length ?
    new Paragraph({
      spacing: { before: 600, after: 80 },
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: data.language === "en" ? "Reviewed through the lens of:" : "Review qua lăng kính của:", italics: true, size: 22, color: "808080" })]
    }) : blank(),
  data.speakers_referenced && data.speakers_referenced.length ?
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: data.speakers_referenced.join("  ·  "), bold: true, size: 22, color: "1F3864" })]
    }) : blank(),
  new Paragraph({ children: [new PageBreak()] })
];

// ===== Part I — Original =====
const partI = data.include_original && data.original ? [
  h1(data.language === "en" ? "PART I — ORIGINAL" : "PHẦN I — BẢN GỐC"),
  p(data.language === "en" ? "Original speech as drafted." : "Bài phát biểu do người trình bày soạn nguyên gốc, trước khi nâng cấp.", { italics: true, color: "595959" }),
  blank(),
  ...data.original.map(renderParagraph),
  new Paragraph({ children: [new PageBreak()] })
] : [];

// ===== Part II — Upgraded =====
const partII = [
  h1(data.language === "en" ? "PART II — UPGRADED VERSION" : "PHẦN II — BẢN NÂNG CẤP"),
  p(data.language === "en"
    ? "This version keeps the speaker's original voice while incorporating rhetorical DNA from legendary public speakers. Stage directions in red italic — do not read aloud."
    : "Bản này giữ giọng của người trình bày, được nâng cấp bằng DNA tu từ của các diễn giả huyền thoại. Ghi chú sân khấu in nghiêng đỏ — không đọc thành tiếng.",
    { italics: true, color: "595959" }),
  blank(),
];

for (const section of (data.upgraded || [])) {
  partII.push(h2(`${section.timestamp || ""}  ${section.title || ""}`.trim()));
  for (const note of (section.stage_notes || [])) {
    partII.push(stageNote(note));
  }
  for (const para of (section.paragraphs || [])) {
    partII.push(renderParagraph(para));
  }
}
partII.push(new Paragraph({ children: [new PageBreak()] }));

// ===== Part III — Stage directions & comparison =====
const partIII = [
  h1(data.language === "en" ? "PART III — DIRECTOR NOTES" : "PHẦN III — GHI CHÚ DÀN DỰNG"),
  p(data.language === "en"
    ? "Director notes and CTA mechanics to maximize audience impact and lead conversion."
    : "Ghi chú dàn dựng sân khấu và cơ chế CTA để tối đa hiệu quả.",
    { italics: true, color: "595959" }),
  blank(),
];

for (const block of (data.stage_directions || [])) {
  partIII.push(h2(block.title));
  for (const b of (block.bullets || [])) {
    partIII.push(bullet(b));
  }
  partIII.push(blank());
}

// Comparison table
if (data.comparison && data.comparison.length > 1) {
  partIII.push(h2(data.language === "en" ? "Side-by-side comparison" : "Bảng so sánh"));
  const header = data.comparison[0];
  const rows = data.comparison.slice(1);
  const colCount = header.length;
  const totalWidth = 9000;
  const firstColWidth = 2200;
  const restWidth = Math.floor((totalWidth - firstColWidth) / (colCount - 1));
  const columnWidths = [firstColWidth, ...Array(colCount - 1).fill(restWidth)];

  partIII.push(new Table({
    width: { size: totalWidth, type: WidthType.DXA },
    columnWidths,
    rows: [
      new TableRow({
        tableHeader: true,
        children: header.map((cell, i) => new TableCell({
          width: { size: columnWidths[i], type: WidthType.DXA },
          shading: { fill: "1F3864", type: ShadingType.CLEAR },
          margins: { top: 100, bottom: 100, left: 120, right: 120 },
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: cell, bold: true, color: "FFFFFF", size: 22 })] })]
        }))
      }),
      ...rows.map(row => new TableRow({
        children: row.map((cell, i) => new TableCell({
          width: { size: columnWidths[i], type: WidthType.DXA },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          children: [new Paragraph({ children: [new TextRun({ text: cell, bold: i === 0, size: 22, color: i === colCount - 1 ? "1F3864" : "000000" })] })]
        }))
      }))
    ]
  }));
  partIII.push(blank());
}

if (data.speakers_referenced && data.speakers_referenced.length) {
  partIII.push(h2(data.language === "en" ? "Referenced speakers" : "Cảm hứng tham chiếu"));
  for (const s of data.speakers_referenced) {
    partIII.push(bullet(s));
  }
}

// ===== Document =====
const doc = new Document({
  creator: data.speaker_name || "Speech Upgrader",
  title: data.event || "Speech",
  styles: {
    default: { document: { run: { font: "Calibri", size: 24 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Calibri", color: "1F3864" },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Calibri", color: "2E75B6" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
    ]
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: (data.event || "Speech") + (data.subtitle ? "  ·  " + data.subtitle : ""), size: 18, color: "808080", italics: true })]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: data.language === "en" ? "Page " : "Trang ", size: 18, color: "808080" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "808080" }),
            new TextRun({ text: " / ", size: 18, color: "808080" }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 18, color: "808080" }),
          ]
        })]
      })
    },
    children: [...cover, ...partI, ...partII, ...partIII]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log("OK:", outputPath);
});
