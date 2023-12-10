from Model.NhanVien import NhanVien


class NhanVienQuanLy(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, he_so_chuc_vu, thuong):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.he_so_chuc_vu = he_so_chuc_vu
        self.thuong = thuong

    def tinh_luong(self):
        luong = self.luong_co_ban * self.he_so_chuc_vu + self.thuong
        return luong
