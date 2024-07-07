def lagrange_interpolation(xs, ys):
    """
    Tính đa thức nội suy Lagrange cho tập điểm (xs, ys).

    Args:
        xs (list): Danh sách các giá trị x của điểm dữ liệu.
        ys (list): Danh sách các giá trị y tương ứng với các giá trị x.

    Returns:
        function: Hàm đa thức nội suy Lagrange.
    """

    # Định nghĩa hàm nội suy Lagrange cho một điểm x cụ thể
    def L(k, x):
        """
        Tính hàm L_k(x) trong đa thức nội suy Lagrange.

        Args:
            k (int): Chỉ số của hàm L_k.
            x (float): Giá trị x để tính L_k(x).

        Returns:
            float: Giá trị của hàm L_k(x) tại x.
        """
        result = 1
        for i in range(len(xs)):
            if i != k:
                result *= (x - xs[i]) / (xs[k] - xs[i])
        return result

    # Tính đa thức nội suy Lagrange cho tất cả các điểm dữ liệu
    def polynomial_interpolation(x):
        """
        Đa thức nội suy Lagrange tại điểm x.

        
            x (float): Giá trị x để tính đa thức nội suy Lagrange.

        Returns:
            float: Giá trị của đa thức nội suy Lagrange tại x.
        """
        lagrange_sum = 0
        for k in range(len(xs)):
            lagrange_sum += ys[k] * L(k, x)
        return lagrange_sum

    return polynomial_interpolation
    
# Ví dụ sử dụng hàm nội suy Lagrange
# Xác định các điểm dữ liệu
p=6899
xs = [1, 3,5]
ys = [(15+6*1+7*1*1)%p, (15+6*2+7*2*2)%p, (15+6*3+7*3*3)%p]
yy = [4682, 2971,3775]
# Tính đa thức nội suy Lagrange
interpolating_poly = lagrange_interpolation(xs, yy)
#5+3*x+15*x2 + 2*x*x*x
# Đánh giá đa thức nội suy Lagrange tại một số điểm x
x_values = [0,1,2]
print(28%17)
print(ys)
for x in x_values:
    print(f"f({x}) = {interpolating_poly(x)}")
