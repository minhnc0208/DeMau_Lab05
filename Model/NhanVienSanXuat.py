from Model.NhanVien import NhanVien


class NhanVienSanXuat(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_san_pham):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_san_pham = so_san_pham

    def tinh_luong(self):
        luong = self.luong_co_ban + self.so_san_pham * 175_000
        thuong = 0.2 * luong if self.so_san_pham > 150 else 0  # Thưởng thêm 20%
        return luong + thuong
