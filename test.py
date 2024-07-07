

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(a, p):
    g, x, _ = extended_gcd(a, p)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    return x % p

def polynomial(x, coefficients, p):
    return sum([coeff * (x ** i) for i, coeff in enumerate(coefficients)]) % p

def chia_se_khoa_shamir(self):
    self.generate_random_p()
    if self.p is None:
        return

    shares = []
    for i in range(1, self.b + 1):
        x = random.randint(1, self.p - 1)
        y = polynomial(x, self.polynomial_coefficients, self.p)
        shares.append((x, y))

    print(f"Shares: {shares}")
    self.hien_thi_shares(shares)

def hien_thi_shares(self, shares):
    model = QtGui.QStandardItemModel()
    model.setHorizontalHeaderLabels(["X", "Y"])
    for x, y in shares:
        x_item = QtGui.QStandardItem(str(x))
        y_item = QtGui.QStandardItem(str(y))
        model.appendRow([x_item, y_item])
    self.table_chia_khoa.setModel(model)

# Kết nối hàm chia sẻ khóa Shamir với sự kiện click của nút
self.btn_chia_se_khoa.clicked.connect(self.chia_se_khoa_shamir)
