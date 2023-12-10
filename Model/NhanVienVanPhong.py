from Model.NhanVien import NhanVien


class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_gio_lam):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_gio_lam = so_gio_lam

    def tinh_luong(self):
        luong = self.luong_co_ban + self.so_gio_lam * 220_000
        tro_cap = 5_000_000 if self.so_gio_lam > 100 else 0
        return luong + tro_cap
