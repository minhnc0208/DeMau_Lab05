# Import các class từ module Model
from Model.NhanVienVanPhong import NhanVienVanPhong
from Model.NhanVienSanXuat import NhanVienSanXuat
from Model.NhanVienQuanLy import NhanVienQuanLy


def main():
    # Câu 1: Khởi tạo dữ liệu
    nhan_vien_vp1 = NhanVienVanPhong(101, "Nguyễn A", 4_500_000, 200)
    nhan_vien_vp2 = NhanVienVanPhong(102, "Nguyễn B", 5_600_000, 100)
    nhan_vien_vp3 = NhanVienVanPhong(103, "Nguyễn C", 8_900_000, 90)

    nhan_vien_sx1 = NhanVienSanXuat(201, "Nguyễn D", 7_800_000, 250)
    nhan_vien_sx2 = NhanVienSanXuat(202, "Nguyễn E", 4_500_000, 110)
    nhan_vien_sx3 = NhanVienSanXuat(203, "Nguyễn F", 6_600_000, 360)

    nhan_vien_ql1 = NhanVienQuanLy(301, "Nguyễn G", 8_500_000, 1.3, 19_500_000)
    nhan_vien_ql2 = NhanVienQuanLy(302, "Nguyễn H", 7_600_000, 1.2, 18_600_000)

    # Tạo danh sách nhân viên
    nhan_viens = [nhan_vien_vp1, nhan_vien_vp2, nhan_vien_vp3, nhan_vien_sx1, nhan_vien_sx2, nhan_vien_sx3,
                  nhan_vien_ql1,
                  nhan_vien_ql2]

    # Câu 4: Tìm kiếm nhân viên theo mã nhân viên
    def tim_kiem_nhan_vien(ma_nv, danh_sach_nhan_vien):
        nv: object
        for nv in danh_sach_nhan_vien:
            if nv.ma_nv == ma_nv:
                return nv
        return None

    # Câu 4: Người dùng nhập mã nhân viên cần tìm
    ma_nv_can_tim = int(input("Nhập mã nhân viên cần tìm: "))

    # Câu 4: Thực hiện tìm kiếm
    nhan_vien_tim_duoc = tim_kiem_nhan_vien(ma_nv_can_tim, nhan_viens)

    # Câu 4: Xuất thông tin nhân viên nếu tìm thấy, ngược lại thông báo không tìm thấy
    if nhan_vien_tim_duoc:
        print(f"Đã tìm thấy nhân viên có mã {ma_nv_can_tim}:")
        print(
            f"Mã NV: {nhan_vien_tim_duoc.ma_nv}, Họ tên: {nhan_vien_tim_duoc.ho_ten}, Lương hằng tháng: {nhan_vien_tim_duoc.tinh_luong()} \n")
    else:
        print(f"Không tìm thấy nhân viên có mã {ma_nv_can_tim}")

    # Câu 5:Tính trung bình tiền lương hằng tháng mà đại lý trả cho NV.
    def tinh_trung_binh_luong(nhan_viens):
        """

        :param nhan_viens:
        :return:
        """
        tong_luong = sum(nv.tinh_luong() for nv in nhan_viens)
        trung_binh_luong = tong_luong / len(nhan_viens)
        return trung_binh_luong

    # Câu 6: Cập nhật lương cơ bản của nhân viên theo mã nhân viên.
    def cap_nhat_luong_co_ban(ma_nv, danh_sach_nhan_vien, luong_moi):
        nhan_vien = tim_kiem_nhan_vien(ma_nv, danh_sach_nhan_vien)
        if nhan_vien:
            nhan_vien.luong_co_ban = luong_moi
            print(f"Đã cập nhật lương cơ bản của nhân viên {ma_nv} thành {luong_moi}")
        else:
            print(f"Không tìm thấy nhân viên có mã {ma_nv}")

    # Xuất lại danh sách nhân viên để kiểm tra cập nhật lương cơ bản
    def xuat_thong_tin_nhan_vien(nhan_viens):
        for nv in nhan_viens:
            print(f"Mã NV: {nv.ma_nv}, Họ tên: {nv.ho_ten}, Lương hằng tháng: {nv.tinh_luong()}")

    print("Toàn bộ thông tin của nhân viên được xuất, bao gồm:")
    for nv in nhan_viens:
        # Câu 2: Xuất thông tin nhân viên & Câu 3: Tính lương cho từng nhân viên
        print(f"Mã NV: {nv.ma_nv}, Họ tên: {nv.ho_ten}, Lương hằng tháng: {nv.tinh_luong()} \n")
        # Câu 3: Tính lương cho từng nhân viên
        # luong_thang = nv.tinh_luong()

    # Câu 5: Tính trung bình lương và xuất kết quả
    trung_binh_luong = tinh_trung_binh_luong(nhan_viens)
    print(f"Trung bình tiền lương hằng tháng mà đại lý trả cho nhân viên: {trung_binh_luong}")

    # Câu 6: Người dùng nhập mã nhân viên và lương mới
    ma_nv_can_cap_nhat = int(input("Nhập mã nhân viên cần cập nhật lương cơ bản: "))
    luong_moi = float(input("Nhập lương cơ bản mới: "))

    # Câu 6: Thực hiện cập nhật lương cơ bản và xuất kết quả
    cap_nhat_luong_co_ban(ma_nv_can_cap_nhat, nhan_viens, luong_moi)

    # Xuất lại danh sách nhân viên để kiểm tra cập nhật lương cơ bản
    print("\nDanh sách nhân viên sau khi cập nhật:")
    xuat_thong_tin_nhan_vien(nhan_viens)


# Gọi hàm main khi chạy chương trình
if __name__ == "__main__":
    main()
