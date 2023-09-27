#\n ngắt xuống dòng và bắt đầu dòng mời.
#\t đẩy nội dung phía sau nó cách 1 tab.
#\a chuông cảnh báo.
#\b xóa bỏ khoảng trắng phía trước nó.
#\xnn với n là 0->9, hoặc a->f hoặc A->F.

print("website: \"www.google.com\"")
print("test: \xAA \xBB \xCC")

#%c	character
#%s	chuỗi
#%i	số nguyên
#%d	số nguyên
#%u	số nguyên
#%o	bát phân
#%x	thập lục phân (in thường)
#%X	thập lục phân (in hoa)
#%e	số mũ  (với e thường)
#%E	số mũ  (với e hoa)
#%f	số thực
#%g	dạng rút gọn của %f and %e
#%G	dạng rút gọn của %f and %E

a = "Nguyen"
b = "Van"
c = "Phuc"

total = "My name is %s %s %s %c" %(a, b, c, "\xAA")
print(total)

#Truy cập tới từng giá trị của chuỗi.
print("Index = 0: ", total[0])
print("Index = -1: ", total[-1])
print("Index 0 -> 5: ", total[0:5])
print("Index -6 -> 26: ", total[-6:26])
print("Index -6 -> : ", total[-6:])

name = 'nguyen \tvan phuc'
print('---------------Capitalize()-----------------')
print("Hàm này có tác dụng in hoa chữ cái đầu tiên của chuỗi: ", name.capitalize())

print('---------------Center()-----------------')
print("chuỗi được hiển thị ở giữa một chuỗi.: ", name.center(20, '*'))
print("chuỗi được hiển thị ở giữa một chuỗi.: ", name.center(20, '%'))

print('---------------Count()-----------------')
print("đếm xem trong chuỗi có bao nhiêu ký tự cần tìm: ", name.count('n'))

print('---------------encode()-----------------')
print("encode (mã hóa) một chuỗi: ", name.encode())

print('---------------decode()-----------------')
string = b'nguyen van phuc'
print("decode (giải mã) một chuỗi: ", string.decode());

print('---------------endswith()-----------------')
print("kiểm tra xem chuỗi có được kết thúc bằng ký tự nào đó hay không: ", name.endswith('c'))
print("kiểm tra xem chuỗi có được kết thúc bằng ký tự nào đó hay không: ", name.endswith('c', 0, 10))

print('---------------expandtabs()-----------------')
print("tìm kiếm thay thế  \\t bằng các ký tự khoảng trắng: ", name.expandtabs())

print('---------------find()-----------------')
print("tìm kiếm một chuỗi trong một chuỗi: ", name.find('uc', 0))

print('---------------index()-----------------')
try:
    print("tương tự như hàm find() chỉ khác duy nhất là nếu như không tìm thấy thì hàm này sẽ gọi exception.", name.index('cc', 0))
except:
    print('Chứa ký tự khác')

print('---------------isalnum()-----------------')
print("Nó sẽ trả về True nếu chuỗi chỉ chứa các ký tự chữ hoặc số: ", name.isalnum())

print('---------------isalpha()-----------------')
print("True nếu chuỗi này chỉ chứa duy các ký tự chữ trong bảng chữ cái: ", name.isalpha())

print('---------------isdigit()-----------------')
print("True nếu chuỗi này chỉ chứa duy các ký tự số : ", name.isdigit())

print('---------------islower()-----------------')
print("chuỗi có phải là in thường hay không?: ", name.islower())

print('---------------isupper()-----------------')
print("chuỗi có phải là in hoa hay không?: ", name.isupper())

print('---------------isnumeric()-----------------')
print("True nếu chuỗi này chỉ chứa duy các ký tự số : ", name.isnumeric())

print('---------------isspace()-----------------')
print("chuỗi có phải chỉ chứa duy nhất các ký tự khoảng trắng không?: ", name.isspace())

print('---------------istitle()-----------------')
print("kiểm tra xem một chuỗi có phải là title hay không: ", name.istitle())

print('---------------join()-----------------')
print("Nối chuỗi: ", '-'.join(name))

print('---------------len()-----------------')
print("Hàm này có tác dụng trả về độ dài của chuỗi.: ", len(name))

print('---------------ljust()-----------------')
print("Trả về chuỗi mới nếu không đủ độ dài yêu cầu: ", name.ljust(20, '-'))

print('---------------rjust()-----------------')
print("Trả về chuỗi mới nếu không đủ độ dài yêu cầu: ", name.rjust(20, '-'))

print('---------------lower()-----------------')
print("Hàm này có tác dụng chuyển đổi chuỗi về dạng in thường: ", name.lower())

print('---------------upper()-----------------')
print("Hàm này có tác dụng chuyển đổi chuỗi về dạng in hoa: ", name.upper())

print('---------------lstrip()-----------------')
print("Hàm này có tác dụng loại bỏ đi các ký tự char ở phía đầu của chuỗi: ", name.lstrip())

print('---------------rstrip()-----------------')
print("Hàm này có tác dụng loại bỏ đi các ký tự char ở phía cuối của chuỗi: ", name.rstrip())

print('---------------strip()-----------------')
print("Hàm này có tác dụng loại bỏ đi các ký tự char ở đầu và cuối của chuỗi: ", name.strip())

print('---------------rfind()-----------------')
print("nó sẽ trả về index của chuỗi cuối cùng tìm được trong chuỗi.: ", name.rfind('n'))

print('---------------rindex()-----------------')
print("Tương tự như hàm index(),nhưng hàm này nó sẽ trả về index của chuỗi cuối cùng tìm được trong chuỗi.: ", name.rindex('n'))

print('---------------replace()-----------------')
print("Hàm này có tác dụng tìm kiếm và thay thế chuỗi tìm được bằng chuỗi mới.: ", name.replace('c', 't', 1))

print('---------------max()-----------------')
print("chữ cái có độ sắp xếp cuối cùng theo bảng chữ cái alphabet nằm trong chuỗi: ", max(name))

print('---------------min()-----------------')
print("chữ cái có độ sắp xếp đầu tiên theo bảng chữ cái alphabet nằm trong chuỗi: ", min(name))

print('---------------title()-----------------')
print("Hàm này có tác dụng chuyển đổi chuỗi sang kiểu title (xem ở trên).: ", name.title())

print('---------------swapcase()-----------------')
print("nghịch đảo ở đây là hoa - thường: ", name.swapcase())

print('---------------zfill()-----------------')
print("như hàm ljust() , nhưng nó sẽ chỉ thêm được các ký tự zero (số 0) và trước chuỗi thôi.: ", name.zfill(17))

print('---------------isdecimal()-----------------')
print("Hàm này có tác dụng gần như hàm isdigit(), nó sẽ trả về True nếu chuỗi cần kiểm tra chỉ chứa các số thập phân, và ngược lại....: ", name.isdecimal())

print('---------------split()-----------------')
print("tách chuối thành các mảng: ", name.split())

print('---------------splitlines()-----------------')
print("Hàm này sẽ tách chuỗi bởi các ký tự \\n.: ", name.splitlines())

print('---------------startswith()-----------------')
print("kiểm tra xem chuỗi hoặc khoảng chuỗi có được bắt đầu bằng ký tự nào đó hay không: ", name.startswith('n'))

print('---------------maketrans()-----------------')
print("tạo ra các translation cho chuỗi", name.maketrans('n', '1'))

print('---------------translate()-----------------')
print("Hàm này có tác dụng thực thi việc dịch chuỗi: ")
inputs = "abcdefghijklmnopqrstuxyz";
outputs = "ABCDEFGHIJKLMNOPQRSTUXYZ";
string = "Vu Thanh Tai";

trans = string.maketrans(inputs, outputs)
print(string.translate(trans))
# Kết quả: VU THANH TAI