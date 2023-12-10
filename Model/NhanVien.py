class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_co_ban):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban

    def tinh_luong(self):
        pass  # Phương thức trừu tượng, sẽ được cài đặt trong các lớp con
