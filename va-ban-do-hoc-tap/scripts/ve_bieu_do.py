#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vẽ biểu đồ cho báo cáo lộ trình du học + tracker, xuất PNG font tiếng Việt.

7 hàm:
    from ve_bieu_do import radar, chi_phi_cot, phan_bo_nuoc, gpa_xu_huong, \
        timeline_lo_trinh, chi_phi_stack, tien_do_tracker

    radar({"STEM": 3.5, "Ngôn ngữ": 2.8, "Xã hội": 3.0, "Năng khiếu": 2.0}, "radar.png")
    chi_phi_cot(truong=[...], tong_chi_phi=[...], ngan_sach=1500, out="chiphi.png")
    phan_bo_nuoc({"Canada": 4, "Úc": 3, "Hà Lan": 2}, "phanbo.png")
    gpa_xu_huong(["Lớp 10", "Lớp 11", "Lớp 12"], [3.0, 3.3, 3.6], "xuhuong.png")
    timeline_lo_trinh([{"ten": "Lớp 10 - HK2", "bat_dau": 0, "do_dai": 4, "mo_ta": "IELTS 5.0"}], "timeline.png")
    chi_phi_stack(truong=[...], hoc_phi=[...], sinh_hoat=[...], chi_phi_an=[...], out="stack.png")
    tien_do_tracker({"Chứng chỉ Anh ngữ": 60, "Hồ sơ ngoại khóa": 30}, "tiendo.png")

Cài đặt nếu thiếu: pip install matplotlib --break-system-packages
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ---- Font hỗ trợ tiếng Việt ----
def _set_font():
    for name in ["DejaVu Sans", "Noto Sans", "Arial Unicode MS"]:
        try:
            fm.findfont(name, fallback_to_default=False)
            plt.rcParams["font.family"] = name
            break
        except Exception:
            continue
    plt.rcParams["axes.unicode_minus"] = False

_set_font()

MAU = "#2563eb"       # xanh dương chủ đạo
MAU_PHU = "#f59e0b"   # cam
MAU_DO = "#dc2626"    # đỏ (đường ngân sách / cảnh báo)
MAU_XANH_LA = "#16a34a"  # xanh lá (hoàn thành tốt)
MAU_XAM = "#94a3b8"   # xám (chi phí ẩn / nền)


def radar(nang_luc: dict, out: str, tieu_de="Năng lực theo nhóm môn (GPA 4.0)"):
    """nang_luc: {'STEM': 3.5, 'Ngôn ngữ': 2.8, ...} thang 0-4."""
    nhan = list(nang_luc.keys())
    gia_tri = list(nang_luc.values())
    n = len(nhan)
    goc = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    gia_tri += gia_tri[:1]
    goc += goc[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(goc, gia_tri, color=MAU, linewidth=2)
    ax.fill(goc, gia_tri, color=MAU, alpha=0.25)
    ax.set_xticks(goc[:-1])
    ax.set_xticklabels(nhan, fontsize=11)
    ax.set_ylim(0, 4)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_title(tieu_de, fontsize=13, pad=20)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def chi_phi_cot(truong: list, tong_chi_phi: list, ngan_sach: float, out: str,
                tieu_de="Tổng chi phí/năm từng trường (triệu VNĐ)"):
    """truong: tên trường; tong_chi_phi: số (triệu VNĐ); ngan_sach: đường giới hạn."""
    mau = [MAU if c <= ngan_sach else MAU_DO for c in tong_chi_phi]
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = range(len(truong))
    thanh = ax.bar(x, tong_chi_phi, color=mau)
    ax.bar_label(thanh, fmt="%.0f", padding=3, fontsize=8.5)
    ax.axhline(ngan_sach, color=MAU_DO, linestyle="--", linewidth=2,
               label=f"Ngân sách gia đình ({ngan_sach:.0f} tr)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(truong, rotation=40, ha="right", fontsize=9)
    ax.set_ylabel("Triệu VNĐ / năm")
    ax.set_title(tieu_de, fontsize=13)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def phan_bo_nuoc(dem_theo_nuoc: dict, out: str,
                 tieu_de="Phân bổ trường gợi ý theo nước"):
    """dem_theo_nuoc: {'Canada': 4, 'Úc': 3, ...}"""
    nhan = list(dem_theo_nuoc.keys())
    so = list(dem_theo_nuoc.values())
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(so, labels=nhan, autopct=lambda p: f"{p*sum(so)/100:.0f}",
           startangle=90, textprops={"fontsize": 11},
           colors=plt.cm.Blues(np.linspace(0.4, 0.9, len(nhan))))
    ax.set_title(tieu_de, fontsize=13)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def gpa_xu_huong(nam: list, gpa: list, out: str, tieu_de="Xu hướng GPA theo năm"):
    """nam: ['Lớp 10','Lớp 11','Lớp 12']; gpa: [3.0, 3.3, 3.6] thang 4.0.
    Dùng ở Bước 1/2 để hội đồng tuyển sinh (và phụ huynh) thấy rõ điểm đang lên hay xuống."""
    fig, ax = plt.subplots(figsize=(8, 4.2))
    # Trục y PHÓNG TO quanh vùng dữ liệu — trục 0-4 đầy đủ làm đường kẻ dán sát mép
    # trên, phẳng lì và xấu. Phóng to để thấy rõ chiều lên/xuống; để trung thực,
    # luôn ghi nhãn số từng điểm và chú thích trục đã phóng to.
    lo, hi = min(gpa), max(gpa)
    pad = max((hi - lo) * 0.6, 0.15)
    y0, y1 = max(0, lo - pad), min(4.0, hi + pad) if hi + pad < 4.0 else 4.05
    ax.set_ylim(y0, y1)
    ax.fill_between(range(len(nam)), gpa, y0, color=MAU, alpha=0.08, zorder=1)
    ax.plot(nam, gpa, marker="o", color=MAU, linewidth=2.5, markersize=9, zorder=3)
    for x, y in zip(nam, gpa):
        ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points", xytext=(0, 11),
                    ha="center", fontsize=11, fontweight="bold")
    # mũi tên tổng kết chiều xu hướng ở góc
    chieu = "▲ đang lên" if gpa[-1] > gpa[0] + 0.02 else ("▼ đang xuống" if gpa[-1] < gpa[0] - 0.02 else "→ đi ngang")
    ax.text(0.99, 0.04, f"{chieu} · trục phóng to {y0:.1f}–{min(y1,4):.1f} để thấy rõ xu hướng",
            transform=ax.transAxes, ha="right", fontsize=8.5, color="#666666")
    ax.set_ylabel("GPA (thang 4.0)")
    ax.set_title(tieu_de, fontsize=13)
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def timeline_lo_trinh(giai_doan: list, out: str, tieu_de="Lộ trình đến ngày nộp hồ sơ"):
    """giai_doan: list các dict {'ten': 'Lớp 10 - HK2', 'bat_dau': 0, 'do_dai': 4, 'mo_ta': 'IELTS 5.0'}
    bat_dau/do_dai tính theo tháng, kể từ hiện tại (0 = tháng này)."""
    fig, ax = plt.subplots(figsize=(10, max(3, 0.7 * len(giai_doan) + 1)))
    mau_list = plt.cm.Blues(np.linspace(0.85, 0.4, len(giai_doan)))
    for i, gd in enumerate(giai_doan):
        ax.barh(i, gd["do_dai"], left=gd["bat_dau"], color=mau_list[i], height=0.55)
        ax.text(gd["bat_dau"] + gd["do_dai"] / 2, i, gd.get("mo_ta", ""),
                ha="center", va="center", fontsize=9, color="white", fontweight="bold")
    ax.set_yticks(range(len(giai_doan)))
    ax.set_yticklabels([gd["ten"] for gd in giai_doan], fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("Số tháng tính từ hiện tại")
    ax.set_title(tieu_de, fontsize=13)
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def chi_phi_stack(truong: list, hoc_phi: list, sinh_hoat: list, chi_phi_an: list, out: str,
                   tieu_de="Cơ cấu chi phí/năm từng trường (triệu VNĐ)"):
    """3 lớp chồng cột mỗi trường: học phí / sinh hoạt / chi phí ẩn (visa, bảo hiểm, vé, đặt cọc quy về năm)."""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    x = np.arange(len(truong))
    hoc_phi = np.array(hoc_phi, dtype=float)
    sinh_hoat = np.array(sinh_hoat, dtype=float)
    chi_phi_an = np.array(chi_phi_an, dtype=float)
    ax.bar(x, hoc_phi, color=MAU, label="Học phí")
    ax.bar(x, sinh_hoat, bottom=hoc_phi, color=MAU_PHU, label="Sinh hoạt phí")
    ax.bar(x, chi_phi_an, bottom=hoc_phi + sinh_hoat, color=MAU_XAM, label="Chi phí ẩn (visa/BH/vé...)")
    ax.set_xticks(x)
    ax.set_xticklabels(truong, rotation=40, ha="right", fontsize=9)
    ax.set_ylabel("Triệu VNĐ / năm")
    ax.set_title(tieu_de, fontsize=13)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def tien_do_tracker(hang_muc: dict, out: str, tieu_de="Tiến độ thực hiện kế hoạch"):
    """hang_muc: {'Chứng chỉ tiếng Anh': 60, 'Hồ sơ ngoại khóa': 30, ...} % hoàn thành 0-100.
    Dùng khi cập nhật tracker định kỳ, không phải ở báo cáo lần đầu."""
    nhan = list(hang_muc.keys())
    gia_tri = list(hang_muc.values())
    fig, ax = plt.subplots(figsize=(9, max(3, 0.6 * len(nhan) + 1)))
    y = np.arange(len(nhan))
    ax.barh(y, [100] * len(nhan), color="#e5e7eb", height=0.5)
    mau = [MAU_XANH_LA if v >= 70 else (MAU_PHU if v >= 35 else MAU_DO) for v in gia_tri]
    ax.barh(y, gia_tri, color=mau, height=0.5)
    for i, v in enumerate(gia_tri):
        ax.text(min(v + 3, 102), i, f"{v:.0f}%", va="center", fontsize=9, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(nhan, fontsize=10)
    ax.set_xlim(0, 115)
    ax.invert_yaxis()
    ax.set_xlabel("% hoàn thành")
    ax.set_title(tieu_de, fontsize=13)
    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


if __name__ == "__main__":
    # Demo nhanh để kiểm tra script chạy được (xuất vào /tmp, không phải outputs)
    radar({"STEM": 3.5, "Ngôn ngữ": 2.8, "Xã hội": 3.0, "Năng khiếu": 2.2}, "/tmp/demo_radar.png")
    chi_phi_cot(["ĐH A (Canada)", "ĐH B (Úc)", "ĐH C (Anh)", "ĐH D (Mỹ)"],
                [900, 1300, 1600, 2100], 1500, "/tmp/demo_chiphi.png")
    phan_bo_nuoc({"Canada": 4, "Úc": 3, "Hà Lan": 2, "Singapore": 2}, "/tmp/demo_phanbo.png")
    gpa_xu_huong(["Lớp 10", "Lớp 11", "Lớp 12 (HK1)"], [2.8, 3.2, 3.5], "/tmp/demo_xuhuong.png")
    timeline_lo_trinh([
        {"ten": "Lớp 11 - HK1", "bat_dau": 0, "do_dai": 4, "mo_ta": "IELTS 5.0"},
        {"ten": "Lớp 11 - HK2", "bat_dau": 4, "do_dai": 4, "mo_ta": "IELTS 5.5 + NK"},
        {"ten": "Lớp 12 - HK1", "bat_dau": 8, "do_dai": 4, "mo_ta": "IELTS 6.5 + Hồ sơ"},
        {"ten": "Lớp 12 - HK2", "bat_dau": 12, "do_dai": 3, "mo_ta": "Nộp hồ sơ"},
    ], "/tmp/demo_timeline.png")
    chi_phi_stack(["ĐH A (Canada)", "ĐH B (Úc)", "ĐH C (Anh)"],
                  [500, 700, 900], [350, 450, 400], [80, 90, 100], "/tmp/demo_stack.png")
    tien_do_tracker({"Chứng chỉ Anh ngữ": 60, "Hồ sơ ngoại khóa": 30, "Chuẩn bị tài chính": 85,
                      "Bài luận": 15}, "/tmp/demo_tiendo.png")
    print("OK - đã xuất 7 biểu đồ demo vào /tmp/")


def diem_mon_cot(nhom_mon: dict, out: str, tieu_de="Điểm trung bình các môn (cả năm)", diem_chuan: float = None):
    """Biểu đồ CỘT điểm theo môn, các môn CÙNG NHÓM đứng cạnh nhau và cùng tông màu.
    Dùng thay cho biểu đồ đường nhiều môn (rối). Mỗi nhóm một tông; trong nhóm các cột
    đậm nhạt dần để vẫn phân biệt được từng môn.

    nhom_mon: dict có thứ tự {'STEM': {'Toán':9.6,'Lý':9.6,...}, 'Ngôn ngữ': {...}, 'Xã hội': {...}}
    diem_chuan: nếu truyền (vd 8.0), vẽ đường ngang tham chiếu 'mốc giỏi'.
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    _set_font()

    # Tông màu theo nhóm — Navy brand cho STEM, các tông trung tính hài hòa cho nhóm khác
    tong = {'STEM': '#26275D', 'Ngôn ngữ': '#B4552D', 'Xã hội': '#2E6B4F', 'Năng khiếu': '#7A6A8A'}
    mau_du_phong = ['#26275D', '#B4552D', '#2E6B4F', '#7A6A8A', '#8A6D3B']

    labels, values, colors, group_spans = [], [], [], []
    idx = 0
    for gi, (nhom, mon) in enumerate(nhom_mon.items()):
        base = tong.get(nhom, mau_du_phong[gi % len(mau_du_phong)])
        n = len(mon)
        start = idx
        for i, (m, d) in enumerate(mon.items()):
            labels.append(m); values.append(d)
            # đậm nhạt dần trong nhóm: pha trắng 0% -> 45%
            f = 0.45 * i / max(n - 1, 1)
            c = mcolors.to_rgb(base)
            colors.append(tuple(ci + (1 - ci) * f for ci in c))
            idx += 1
        group_spans.append((nhom, start, idx - 1))

    xs = []
    pos = 0
    for nhom, mon in nhom_mon.items():
        for _ in mon:
            xs.append(pos); pos += 1
        pos += 0.6

    fig, ax = plt.subplots(figsize=(max(8, len(labels) * 0.95), 5.2))
    bars = ax.bar(xs, values, color=colors, width=0.8, zorder=3)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.12, f'{v:g}', ha='center', fontsize=10, zorder=4)
    if diem_chuan:
        ax.axhline(diem_chuan, color='#999999', linestyle='--', linewidth=1.2, zorder=2)
        ax.text(xs[-1] + 0.5, diem_chuan, f'mốc {diem_chuan:g}', va='center', fontsize=9, color='#666666')
    # nhãn nhóm dưới trục
    for nhom, s, e in group_spans:
        mid = (xs[s] + xs[e]) / 2
        ax.text(mid, -1.55, nhom, ha='center', fontsize=11, fontweight='bold', color=tong.get(nhom, '#333333'))
    ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, 10.8); ax.set_ylabel('Điểm trung bình cả năm (thang 10)')
    ax.set_title(tieu_de, fontsize=14, pad=12)
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='y', alpha=0.25, zorder=0)
    plt.tight_layout()
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
