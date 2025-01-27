knowledge_graph = {
	('Tên thẻ', 'Hạng thẻ', 'Mã BIN', 'Độ dài số thẻ', 'Hình ảnh thẻ'): {
		'Thẻ Mastercard Ready': ('Hạng Chuẩn - Classic', 511957.0, '16 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_e0cfd3c9f8024f569645c70c9d26e6fd.png'),
		'Thẻ Mastercard Discovery': ('Hạng Bạch Kim - Platinum', 517453.0, '16 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_f907480c231b4c31a7f5a9fcbf237b4e.jpg'),
		'Thẻ liên kết': ('Không xác định', 970418.0, '19 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_e571fde71d8c47d2896cfce4d6305c52.jpg'),
		'Thẻ X Smart chip': ('Không xác định', 970418.0, '19 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_dab0c50f022847db883c11860760942c.jpg'),
	},
	('Hạng thẻ', 'Tên thẻ', 'Mã BIN', 'Độ dài số thẻ', 'Hình ảnh thẻ'): {
		'Hạng Chuẩn - Classic': ('Thẻ Mastercard Ready', 511957.0, '16 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_e0cfd3c9f8024f569645c70c9d26e6fd.png'),
		'Hạng Bạch Kim - Platinum': ('Thẻ Mastercard Discovery', 517453.0, '16 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_f907480c231b4c31a7f5a9fcbf237b4e.jpg'),
		'Không xác định': ('Thẻ X Smart chip', 970418.0, '19 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_dab0c50f022847db883c11860760942c.jpg'),
	},
	('Mã BIN', 'Tên thẻ', 'Hạng thẻ', 'Độ dài số thẻ', 'Hình ảnh thẻ'): {
		'511957.0': ('Thẻ Mastercard Ready', 'Hạng Chuẩn - Classic', '16 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_e0cfd3c9f8024f569645c70c9d26e6fd.png'),
		'517453.0': ('Thẻ Mastercard Discovery', 'Hạng Bạch Kim - Platinum', '16 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_f907480c231b4c31a7f5a9fcbf237b4e.jpg'),
		'970418.0': ('Thẻ X Smart chip', 'Không xác định', '19 số', '8637e054-8e2b-4209-892c-df8ebe5f5369_dab0c50f022847db883c11860760942c.jpg'),
	},
	('Độ dài số thẻ', 'Tên thẻ', 'Hạng thẻ', 'Mã BIN', 'Hình ảnh thẻ'): {
		'16 số': ('Thẻ Mastercard Discovery', 'Hạng Bạch Kim - Platinum', 517453.0, '8637e054-8e2b-4209-892c-df8ebe5f5369_f907480c231b4c31a7f5a9fcbf237b4e.jpg'),
		'19 số': ('Thẻ X Smart chip', 'Không xác định', 970418.0, '8637e054-8e2b-4209-892c-df8ebe5f5369_dab0c50f022847db883c11860760942c.jpg'),
	},
	('Hình ảnh thẻ', 'Tên thẻ', 'Hạng thẻ', 'Mã BIN', 'Độ dài số thẻ'): {
		'8637e054-8e2b-4209-892c-df8ebe5f5369_e0cfd3c9f8024f569645c70c9d26e6fd.png': ('Thẻ Mastercard Ready', 'Hạng Chuẩn - Classic', 511957.0, '16 số'),
		'8637e054-8e2b-4209-892c-df8ebe5f5369_f907480c231b4c31a7f5a9fcbf237b4e.jpg': ('Thẻ Mastercard Discovery', 'Hạng Bạch Kim - Platinum', 517453.0, '16 số'),
		'8637e054-8e2b-4209-892c-df8ebe5f5369_e571fde71d8c47d2896cfce4d6305c52.jpg': ('Thẻ liên kết', 'Không xác định', 970418.0, '19 số'),
		'8637e054-8e2b-4209-892c-df8ebe5f5369_dab0c50f022847db883c11860760942c.jpg': ('Thẻ X Smart chip', 'Không xác định', 970418.0, '19 số'),
	},
	('Tên thẻ', 'Tên thẻ thay thế'): {
		'Thẻ Mastercard Premier mã 12': ('Thẻ Mastercard Ready',),
		'Thẻ MasterCard Young Plus mã 22-33': ('Thẻ Mastercard Ready',),
	},
	('Tên thẻ thay thế', 'Tên thẻ'): {
		'Thẻ Mastercard Ready': ('Thẻ MasterCard Young Plus mã 22-33',),
	},
	('Mã SP', 'Mã SP tại Corebanking mới'): {
		'I5-CB TONG CONG TY ACV': ('DP01-OLD_Thẻ Chip VL ACV',),
		'I7-NGUOI NHAN TRO CAP ASXH': ('DP03-OLD_Thẻ Chip VL ASXH',),
		'B0-THE LIEN KET CHIP': ('DS04-OLD_Thẻ Chip VL Liên kết',),
		'B6-THE LIEN KET CHIP': ('DS04-OLD_Thẻ Chip VL Liên kết',),
		'B1-THE PHI VAT LY': ('DG05-OLD_Thẻ Chip Phi Vật lý',),
		'B2-THE PHI VAT LY': ('DG05-OLD_Thẻ Chip Phi Vật lý',),
		'B3-THE PHI VAT LY': ('DG05-OLD_Thẻ Chip Phi Vật lý',),
		'B4-THE VAT LY ONLINE': ('DG06-OLD_Thẻ Chip VL online',),
		'B5-THE VAT LY ONLINE': ('DG06-OLD_Thẻ Chip VL online',),
		'I0-Cho KH trả lương và vãng lai': ('DG07-OLD_Thẻ Chip VL',),
		'I1-Cho KH trả lương và vãng lai': ('DG07-OLD_Thẻ Chip VL',),
		'I2-KH VANG LAI': ('DG07-OLD_Thẻ Chip VL',),
		'I3-KH VANG LAI': ('DG07-OLD_Thẻ Chip VL',),
		'I4-KH VANG LAI': ('DG07-OLD_Thẻ Chip VL',),
		'I8-KHACH HANG SU DUNG TK USD': ('DG07-OLD_Thẻ Chip VL',),
		'I9-KHACH HANG SU DUNG TK USD': ('DG07-OLD_Thẻ Chip VL',),
		'B7-Cho KH trả lương và vãng lai': ('DG07-OLD_Thẻ Chip VL',),
		'B8-Cho KH trả lương và vãng lai': ('DG07-OLD_Thẻ Chip VL',),
		'B9-THE CHUYEN DOI B9': ('DG08-OLD_Thẻ Chip VL CD',),
		'D9-THE CHUYEN DOI D9': ('DG08-OLD_Thẻ Chip VL CD',),
		'D2-THE CHUYEN DOI D2': ('DG08-OLD_Thẻ Chip VL CD',),
		'D3-THE CHUYEN DOI D3': ('DG09-OLD_Thẻ Chip Phi VL',),
		'D4-THE CHUYEN DOI D4': ('DG09-OLD_Thẻ Chip Phi VL',),
		'A1-ACV CARDD-CTY CANG HANG KHONG VN': ('MP01-Thẻ từ ACV',),
		'A2-THE GOERTEK VINA': ('MP02-Thẻ từ Goertek',),
		'A3-THE NHAN TRO CAP (ASXH)': ('MP03-Thẻ từ ASXH',),
		'PA-HARMONY CARD': ('MP04-Thẻ từ Harmony',),
		'T1-FOR FOREIGN CURRENCY CARD': ('MP04-Thẻ từ Harmony',),
		'G3-ETRANS GOLD CARD': ('MG05-Thẻ từ Etrans',),
		'SP-ETRANS SILVER CARD': ('MG05-Thẻ từ Etrans',),
		'V6-FOR FOREIGN CURRENCY CARD': ('MG05-Thẻ từ Etrans',),
		'GC-FOR CONNECT CARDS': ('MG05-Thẻ từ Etrans',),
		'GM-THE TRA LUONG UU DAI': ('MG05-Thẻ từ Etrans',),
		'F1-THE THU PHI THEO GOI DVBL': ('MG05-Thẻ từ Etrans',),
		'S1-MOVING SILVER CARD': ('MS06-Thẻ từ Moving',),
		'SU-FOR NORMAL CARDS': ('SU-FOR NORMAL CARDS',),
		'SY-THE LIEN KET SINH VIEN': ('SY-THE LIEN KET SINH VIEN',),
	},
	('Mã SP tại Corebanking mới', 'Mã SP'): {
		'DP01-OLD_Thẻ Chip VL ACV': ('I5-CB TONG CONG TY ACV',),
		'DP03-OLD_Thẻ Chip VL ASXH': ('I7-NGUOI NHAN TRO CAP ASXH',),
		'DS04-OLD_Thẻ Chip VL Liên kết': ('B6-THE LIEN KET CHIP',),
		'DG05-OLD_Thẻ Chip Phi Vật lý': ('B3-THE PHI VAT LY',),
		'DG06-OLD_Thẻ Chip VL online': ('B5-THE VAT LY ONLINE',),
		'DG07-OLD_Thẻ Chip VL': ('B8-Cho KH trả lương và vãng lai',),
		'DG08-OLD_Thẻ Chip VL CD': ('D2-THE CHUYEN DOI D2',),
		'DG09-OLD_Thẻ Chip Phi VL': ('D4-THE CHUYEN DOI D4',),
		'MP01-Thẻ từ ACV': ('A1-ACV CARDD-CTY CANG HANG KHONG VN',),
		'MP02-Thẻ từ Goertek': ('A2-THE GOERTEK VINA',),
		'MP03-Thẻ từ ASXH': ('A3-THE NHAN TRO CAP (ASXH)',),
		'MP04-Thẻ từ Harmony': ('T1-FOR FOREIGN CURRENCY CARD',),
		'MG05-Thẻ từ Etrans': ('F1-THE THU PHI THEO GOI DVBL',),
		'MS06-Thẻ từ Moving': ('S1-MOVING SILVER CARD',),
		'SU-FOR NORMAL CARDS': ('SU-FOR NORMAL CARDS',),
		'SY-THE LIEN KET SINH VIEN': ('SY-THE LIEN KET SINH VIEN',),
	},
	('Tính năng nổi bật', 'Tên thẻ', 'Chi tiết tính năng'): {
		'Tích lũy điểm thưởng': ('Thẻ Mastercard Discovery', 'Tích điểm 2% khi giao dịch ngoại tệ và 0.15% với các giao dịch còn lại, trừ giao dịch đặc thù'),
		'Mua hàng trả góp': ('Thẻ tín dụng cá nhân các hạng', 'Cho phép chuyển đổi giao dịch mua sắm hàng hóa, dịch vụ hợp lệ bất kỳ thành giao dịch trả góp với kỳ hạn trả góp và giá trị giao dịch tối thiểu theo quy định của X trong từng thời kỳ'),
		'Tặng đặc quyền miễn phí': ('Thẻ JCB Credit Ultimate', 'Quyền lợi sử dụng phòng chờ, và các ưu đãi ẩm thực, golf, khách sạn theo chính sách của JCB theo từng thời kỳ'),
		'Dịch vụ hỗ trợ khách hàng 24-7': ('Thẻ ghi nợ và tín dụng doanh nghiệp', 'Điện thoại: 1900 9247 - trong nước hoặc 84 24 22200588 - nước ngoài và Email: bidv247@bidv.com.vn'),
		'Dịch vụ tin nhắn BSMS': ('Thẻ ghi nợ và tín dụng doanh nghiệp', 'Đối với tổ chức đăng ký phát hành thẻ: Yêu cầu tổ chức đăng ký BSMS cho tất cả thẻ tín dụng doanh nghiệp của tổ chức và thu phí từ tài khoản thanh toán của tổ chức|Đối với cá nhân đang sử dụng BSMS mà không thay đổi SĐT, không phát sinh thêm SĐT khác nhận tin thì thu phí theo gói BSMS cá nhân đã sử dụng|Đối với cá nhân chưa sử dụng BSMS hoặc thay đổi, bổ sung SĐT khác nhận tin: KH trả phí dịch vụ BSMS theo quy định tại biểu phí KHCN từng thời kỳ'),
	},
	('Tên thẻ', 'Tính năng nổi bật', 'Chi tiết tính năng'): {
		'Thẻ Mastercard Discovery': ('Tích lũy điểm thưởng', 'Tích điểm 2% khi giao dịch ngoại tệ và 0.15% với các giao dịch còn lại, trừ giao dịch đặc thù'),
		'Thẻ tín dụng cá nhân các hạng': ('Mua hàng trả góp', 'Cho phép chuyển đổi giao dịch mua sắm hàng hóa, dịch vụ hợp lệ bất kỳ thành giao dịch trả góp với kỳ hạn trả góp và giá trị giao dịch tối thiểu theo quy định của X trong từng thời kỳ'),
		'Thẻ JCB Credit Ultimate': ('Tặng đặc quyền miễn phí', 'Quyền lợi sử dụng phòng chờ, và các ưu đãi ẩm thực, golf, khách sạn theo chính sách của JCB theo từng thời kỳ'),
		'Thẻ ghi nợ và tín dụng doanh nghiệp': ('Dịch vụ tin nhắn BSMS', 'Đối với tổ chức đăng ký phát hành thẻ: Yêu cầu tổ chức đăng ký BSMS cho tất cả thẻ tín dụng doanh nghiệp của tổ chức và thu phí từ tài khoản thanh toán của tổ chức|Đối với cá nhân đang sử dụng BSMS mà không thay đổi SĐT, không phát sinh thêm SĐT khác nhận tin thì thu phí theo gói BSMS cá nhân đã sử dụng|Đối với cá nhân chưa sử dụng BSMS hoặc thay đổi, bổ sung SĐT khác nhận tin: KH trả phí dịch vụ BSMS theo quy định tại biểu phí KHCN từng thời kỳ'),
	},
	('Chi tiết tính năng', 'Tính năng nổi bật', 'Tên thẻ'): {
		'Tích điểm 2% khi giao dịch ngoại tệ và 0.15% với các giao dịch còn lại, trừ giao dịch đặc thù': ('Tích lũy điểm thưởng', 'Thẻ Mastercard Discovery'),
		'Cho phép chuyển đổi giao dịch mua sắm hàng hóa, dịch vụ hợp lệ bất kỳ thành giao dịch trả góp với kỳ hạn trả góp và giá trị giao dịch tối thiểu theo quy định của X trong từng thời kỳ': ('Mua hàng trả góp', 'Thẻ tín dụng cá nhân các hạng'),
		'Quyền lợi sử dụng phòng chờ, và các ưu đãi ẩm thực, golf, khách sạn theo chính sách của JCB theo từng thời kỳ': ('Tặng đặc quyền miễn phí', 'Thẻ JCB Credit Ultimate'),
		'Điện thoại: 1900 9247 - trong nước hoặc 84 24 22200588 - nước ngoài và Email: bidv247@bidv.com.vn': ('Dịch vụ hỗ trợ khách hàng 24-7', 'Thẻ ghi nợ và tín dụng doanh nghiệp'),
		'Đối với tổ chức đăng ký phát hành thẻ: Yêu cầu tổ chức đăng ký BSMS cho tất cả thẻ tín dụng doanh nghiệp của tổ chức và thu phí từ tài khoản thanh toán của tổ chức|Đối với cá nhân đang sử dụng BSMS mà không thay đổi SĐT, không phát sinh thêm SĐT khác nhận tin thì thu phí theo gói BSMS cá nhân đã sử dụng|Đối với cá nhân chưa sử dụng BSMS hoặc thay đổi, bổ sung SĐT khác nhận tin: KH trả phí dịch vụ BSMS theo quy định tại biểu phí KHCN từng thời kỳ': ('Dịch vụ tin nhắn BSMS', 'Thẻ ghi nợ và tín dụng doanh nghiệp'),
	},
	('Thông tin chung về thẻ', 'Loại thẻ', 'Thông tin chi tiết'): {
		'Mô tả sản phẩm': ('Thẻ ghi nợ cá nhân', 'Là thẻ do X phát hành gồm Thẻ ghi nợ nội địa - thẻ có BIN do Ngân hàng Nhà nước cấp và Thẻ ghi nợ quốc tế - thẻ có BIN do Tổ chức thẻ quốc tế cấp'),
		'Tài khoản liên kết': ('Thẻ ghi nợ cá nhân', 'Là tài khoản tiền gửi thanh toán cá nhân VND hoặc ngoại tệ USD thuộc sở hữu, sở hữu chung của Chủ thẻ theo quy định từng sản phẩm'),
		'Hạn mức giao dịch hoặc hạn mức tín dụng': ('Thẻ ghi nợ cá nhân', 'Được xác định theo từng loại sản phẩm, loại giao dịch, phạm vi giao dịch|Đối với hạn mức rút ngoại tệ tiền mặt tại nước ngoài, một thẻ được rút số ngoại tệ tối đa tương đương 30 triệu đồng trong 1 ngày|Hạn mức giao dịch thanh toán không tiếp xúc và không cần nhập PIN đối với Thẻ Ghi nợ nội địa là tối đa 500.000VND 1 lần, tối đa 1.000.000VND 1 ngày, không giới hạn số lần 1 ngày'),
		'Kênh thanh toán dư nợ': ('Thẻ tín dụng cá nhân', 'Thanh toán tại quầy|Trích nợ tự động|Chuyển khoản từ ngân hàng khác trong và ngoài nước tới X|Ứng dụng X Smartbanking'),
		'Số lượng thẻ phát hành tối đa theo KH': ('Thẻ tín dụng cá nhân', 'Mỗi cá nhân được phát hành 01 thẻ chính cho 1 mã sản phẩm thẻ, mỗi chủ thẻ chính được phát hành tối đa 03 thẻ phụ; chủ thẻ chính và các chủ thẻ phụ phải là các cá nhân khác nhau'),
		'Phân loại sản phẩm': ('Thẻ tín dụng cá nhân', 'Gồm có 12 sản phẩm thẻ chia làm các hạng: hạng cao cấp bao gồm: Infinite, Signature, Ultimate; hạng Platinum; hạng Gold và hạng Classic'),
	},
	('Loại thẻ', 'Thông tin chung về thẻ', 'Thông tin chi tiết'): {
		'Thẻ ghi nợ cá nhân': ('Hạn mức giao dịch hoặc hạn mức tín dụng', 'Được xác định theo từng loại sản phẩm, loại giao dịch, phạm vi giao dịch|Đối với hạn mức rút ngoại tệ tiền mặt tại nước ngoài, một thẻ được rút số ngoại tệ tối đa tương đương 30 triệu đồng trong 1 ngày|Hạn mức giao dịch thanh toán không tiếp xúc và không cần nhập PIN đối với Thẻ Ghi nợ nội địa là tối đa 500.000VND 1 lần, tối đa 1.000.000VND 1 ngày, không giới hạn số lần 1 ngày'),
		'Thẻ tín dụng cá nhân': ('Phân loại sản phẩm', 'Gồm có 12 sản phẩm thẻ chia làm các hạng: hạng cao cấp bao gồm: Infinite, Signature, Ultimate; hạng Platinum; hạng Gold và hạng Classic'),
	},
	('Thông tin chi tiết', 'Thông tin chung về thẻ', 'Loại thẻ'): {
		'Là thẻ do X phát hành gồm Thẻ ghi nợ nội địa - thẻ có BIN do Ngân hàng Nhà nước cấp và Thẻ ghi nợ quốc tế - thẻ có BIN do Tổ chức thẻ quốc tế cấp': ('Mô tả sản phẩm', 'Thẻ ghi nợ cá nhân'),
		'Là tài khoản tiền gửi thanh toán cá nhân VND hoặc ngoại tệ USD thuộc sở hữu, sở hữu chung của Chủ thẻ theo quy định từng sản phẩm': ('Tài khoản liên kết', 'Thẻ ghi nợ cá nhân'),
		'Được xác định theo từng loại sản phẩm, loại giao dịch, phạm vi giao dịch|Đối với hạn mức rút ngoại tệ tiền mặt tại nước ngoài, một thẻ được rút số ngoại tệ tối đa tương đương 30 triệu đồng trong 1 ngày|Hạn mức giao dịch thanh toán không tiếp xúc và không cần nhập PIN đối với Thẻ Ghi nợ nội địa là tối đa 500.000VND 1 lần, tối đa 1.000.000VND 1 ngày, không giới hạn số lần 1 ngày': ('Hạn mức giao dịch hoặc hạn mức tín dụng', 'Thẻ ghi nợ cá nhân'),
		'Thanh toán tại quầy|Trích nợ tự động|Chuyển khoản từ ngân hàng khác trong và ngoài nước tới X|Ứng dụng X Smartbanking': ('Kênh thanh toán dư nợ', 'Thẻ tín dụng cá nhân'),
		'Mỗi cá nhân được phát hành 01 thẻ chính cho 1 mã sản phẩm thẻ, mỗi chủ thẻ chính được phát hành tối đa 03 thẻ phụ; chủ thẻ chính và các chủ thẻ phụ phải là các cá nhân khác nhau': ('Số lượng thẻ phát hành tối đa theo KH', 'Thẻ tín dụng cá nhân'),
		'Gồm có 12 sản phẩm thẻ chia làm các hạng: hạng cao cấp bao gồm: Infinite, Signature, Ultimate; hạng Platinum; hạng Gold và hạng Classic': ('Phân loại sản phẩm', 'Thẻ tín dụng cá nhân'),
	},
	('Loại thẻ', 'Lợi ích KH'): {
		'Thẻ ghi nợ nội địa cá nhân': ('Tận dụng được các ưu đãi, khuyến mại của ngân hàng, tổ chức thẻ và các đối tác liên kết',),
		'Thẻ tín dụng cá nhân': ('Tận dụng nguồn vốn của ngân hàng với thời gian ân hạn theo chính sách từng thời kỳ',),
		'Thẻ trả trước vô danh': ('Đăng ký thẻ trả trước vô danh như thẻ quà tặng nhưng chưa có nhu cầu đăng ký thông tin cá nhân định danh tại Ngân hàng',),
		'Thẻ trả trước định danh': ('Thủ tục phát hành thẻ và nhận thẻ đơn giản so với các sản phẩm thẻ ghi nợ và tín dụng quốc tế',),
		'Thẻ ghi nợ doanh nghiệp': ('Dễ dàng thanh toán tại hàng chục triệu điểm chấp nhận thẻ trên toàn cầu',),
		'Thẻ tín dụng doanh nghiệp': ('Chi tiêu trước, trả tiền sau, miễn lãi đến 45 ngày',),
	},
	('Lợi ích KH', 'Loại thẻ'): {
		'An toàn, thuận tiện khi thanh toán, loại bỏ rủi ro khi mang theo tiền mặt': ('Thẻ ghi nợ nội địa cá nhân',),
		'Gia tăng bảo mật với công nghệ Chip theo chuẩn EVM-VCCS và trải nghiệm thanh toán liền mạch với tính năng thanh toán không chạm: contactless': ('Thẻ ghi nợ nội địa cá nhân',),
		'Quản lý chi tiêu dễ dàng thông qua các chương trình phần mềm, tin nhắn SMS-OTT, email, Smartbanking': ('Thẻ ghi nợ nội địa cá nhân',),
		'Tận dụng được các ưu đãi, khuyến mại của ngân hàng, tổ chức thẻ và các đối tác liên kết': ('Thẻ ghi nợ nội địa cá nhân',),
		'Thuận tiện khi thanh toán': ('Thẻ tín dụng cá nhân',),
		'Tận dụng được các đặc quyền, ưu đãi khuyến mại của ngân hàng, tổ chức thẻ quốc tế và các đối tác liên kết': ('Thẻ tín dụng cá nhân',),
		'Tận dụng nguồn vốn của ngân hàng với thời gian ân hạn theo chính sách từng thời kỳ': ('Thẻ tín dụng cá nhân',),
		'Đăng ký thẻ trả trước vô danh như thẻ quà tặng nhưng chưa có nhu cầu đăng ký thông tin cá nhân định danh tại Ngân hàng': ('Thẻ trả trước vô danh',),
		'Đăng ký phát hành và sử dụng thẻ quốc tế mang thương hiệu Visa nhanh chóng, thuận tiện, quản lý chi tiêu trong phạm vi số dư tiền trên thẻ mà khách hàng mong muốn sử dụng': ('Thẻ trả trước định danh',),
		'Thủ tục phát hành thẻ và nhận thẻ đơn giản so với các sản phẩm thẻ ghi nợ và tín dụng quốc tế': ('Thẻ trả trước định danh',),
		'Đơn giản hóa thủ tục hành chính khi tạm ứng công tác phí': ('Thẻ ghi nợ doanh nghiệp',),
		'Không cần quy đổi ngoại tệ khi cán bộ đi công tác nước ngoài': ('Thẻ ghi nợ doanh nghiệp',),
		'Dễ dàng thanh toán tại hàng chục triệu điểm chấp nhận thẻ trên toàn cầu': ('Thẻ ghi nợ doanh nghiệp',),
		'Chi tiêu trước, trả tiền sau, miễn lãi đến 45 ngày': ('Thẻ tín dụng doanh nghiệp',),
	},
	('Tên thẻ', 'Trạng thái thẻ', 'Các loại khách hàng', 'Mã SP', 'Loại thẻ', 'Đặc điểm chi tiết thẻ', 'Hình thức thẻ'): {
	},
	('Trạng thái thẻ', 'Tên thẻ', 'Các loại khách hàng', 'Mã SP', 'Loại thẻ', 'Đặc điểm chi tiết thẻ', 'Hình thức thẻ'): {
	},
	('Các loại khách hàng', 'Tên thẻ', 'Trạng thái thẻ', 'Mã SP', 'Loại thẻ', 'Đặc điểm chi tiết thẻ', 'Hình thức thẻ'): {
	},
	('Mã SP', 'Tên thẻ', 'Trạng thái thẻ', 'Các loại khách hàng', 'Loại thẻ', 'Đặc điểm chi tiết thẻ', 'Hình thức thẻ'): {
	},
	('Loại thẻ', 'Tên thẻ', 'Trạng thái thẻ', 'Các loại khách hàng', 'Mã SP', 'Đặc điểm chi tiết thẻ', 'Hình thức thẻ'): {
	},
	('Đặc điểm chi tiết thẻ', 'Tên thẻ', 'Trạng thái thẻ', 'Các loại khách hàng', 'Mã SP', 'Loại thẻ', 'Hình thức thẻ'): {
	},
	('Hình thức thẻ', 'Tên thẻ', 'Trạng thái thẻ', 'Các loại khách hàng', 'Mã SP', 'Loại thẻ', 'Đặc điểm chi tiết thẻ'): {
	},
	('Loại giao dịch', 'Loại thẻ', 'Chi tiết giao dịch'): {
		'Trên máy ATM': ('Thẻ trả trước định danh', 'Thanh toán hàng hóa dịch vụ hoặc Rút tiền mặt tại tất cả các ATM, POS, Máy giao dịch tự động có biểu tượng tương ứng biểu tượng trên thẻ'),
		'Trên thiết bị chấp nhận thanh toán POS': ('Thẻ trả trước định danh', 'Thanh toán hàng hóa dịch vụ hoặc Rút tiền mặt tại tất cả các ATM, POS, Máy giao dịch tự động có biểu tượng tương ứng biểu tượng trên thẻ'),
	},
	('Loại thẻ', 'Loại giao dịch', 'Chi tiết giao dịch'): {
		'Thẻ ghi nợ nội địa cá nhân vật lý': ('Trên thiết bị chấp nhận thanh toán POS', 'Giao dịch hủy'),
		'Thẻ trả trước vô danh': ('Trên máy ATM', 'Chỉ áp dụng thanh toán hàng hóa dịch vụ  trên thiết bị POS có biểu tượng VISA trong nước'),
		'Thẻ trả trước định danh': ('Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ hoặc Rút tiền mặt tại tất cả các ATM, POS, Máy giao dịch tự động có biểu tượng tương ứng biểu tượng trên thẻ'),
	},
	('Chi tiết giao dịch', 'Loại giao dịch', 'Loại thẻ'): {
		'Rút tiền mặt bằng thẻ': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Đổi PIN': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Vấn tin số dư tài khoản': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'In sao kê rút gọn, in hóa đơn giao dịch': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Chuyển tiền từ tài khoản liên kết thẻ đến tài khoản, thẻ ngân hàng khác trong liên minh Napas theo thời gian thực, ngoại trừ tài khoản ngoại tệ': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Nhận chuyển tiền từ tài khoản, thẻ ngân hàng khác trong liên minh Napas tới số thẻ theo thời gian thực, ngoại trừ tài khoản ngoại tệ': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Thanh toán hoá đơn': ('Trên máy ATM', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Thanh toán hàng hóa dịch vụ': ('Trên thiết bị chấp nhận thanh toán POS', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Giao dịch hủy': ('Trên thiết bị chấp nhận thanh toán POS', 'Thẻ ghi nợ nội địa cá nhân vật lý'),
		'Không áp dụng ứng hoặc rút tiền mặt': ('Trên máy ATM', 'Thẻ trả trước vô danh'),
		'Không áp dụng thanh toán trực tuyến E-commerce': ('Trên máy ATM', 'Thẻ trả trước vô danh'),
		'Chỉ áp dụng thanh toán hàng hóa dịch vụ  trên thiết bị POS có biểu tượng VISA trong nước': ('Trên máy ATM', 'Thẻ trả trước vô danh'),
		'Thanh toán hàng hóa dịch vụ hoặc Rút tiền mặt tại tất cả các ATM, POS, Máy giao dịch tự động có biểu tượng tương ứng biểu tượng trên thẻ': ('Trên thiết bị chấp nhận thanh toán POS', 'Thẻ trả trước định danh'),
	},
	('Loại hạn mức', 'Chi tiết hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Tên thẻ', 'Các loại khách hàng'): {
		'Số tiền tối đa/lần': ('1.000.000.000 VNĐ', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức cao'),
		'Số tiền tối đa/ngày': ('100.000.000 VNĐ', 'Trên máy ATM', 'Chuyển tiền nhanh liên ngân hàng 24/7', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
	},
	('Chi tiết hạn mức', 'Loại hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Tên thẻ', 'Các loại khách hàng'): {
		'5.000.000 VNĐ': ('Số tiền tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
		'Trong nước: 200.000.000 VNĐ, nước ngoài: 30.000.000 VNĐ': ('Số tiền tối đa/ngày', 'Trên máy ATM', 'Rút tiền mặt bằng thẻ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức thông thường'),
		'Trong nước: 400.000.000 VNĐ, nước ngoài: 30.000.000 VNĐ': ('Số tiền tối đa/ngày', 'Trên máy ATM', 'Rút tiền mặt bằng thẻ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức cao'),
		'500.000.000 VNĐ': ('Số tiền tối đa/lần', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức thông thường'),
		'1.000.000.000 VNĐ': ('Số tiền tối đa/lần', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức cao'),
		'10.000.000 VNĐ': ('Số tiền tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
		'100.000.000 VNĐ': ('Số tiền tối đa/ngày', 'Trên máy ATM', 'Chuyển tiền nhanh liên ngân hàng 24/7', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
	},
	('Loại giao dịch', 'Loại hạn mức', 'Chi tiết hạn mức', 'Chi tiết giao dịch', 'Tên thẻ', 'Các loại khách hàng'): {
		'Trên máy ATM': ('Số tiền tối đa/ngày', '100.000.000 VNĐ', 'Chuyển tiền nhanh liên ngân hàng 24/7', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
		'Trên thiết bị chấp nhận thanh toán POS': ('Số tiền tối đa/ngày', '10.000.000 VNĐ', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
	},
	('Chi tiết giao dịch', 'Loại hạn mức', 'Chi tiết hạn mức', 'Loại giao dịch', 'Tên thẻ', 'Các loại khách hàng'): {
		'Rút tiền mặt bằng thẻ': ('Số tiền tối đa/lần', '5.000.000 VNĐ', 'Trên thiết bị chấp nhận thanh toán POS', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức cao'),
		'Chuyển khoản': ('Số tiền tối đa/ngày', '10.000.000 VNĐ', 'Trên máy ATM', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
		'Thanh toán hàng hóa dịch vụ': ('Số tiền tối đa/ngày', '10.000.000 VNĐ', 'Trên thiết bị chấp nhận thanh toán POS', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
		'Chuyển tiền nhanh liên ngân hàng 24/7': ('Số tiền tối đa/ngày', '100.000.000 VNĐ', 'Trên máy ATM', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
	},
	('Tên thẻ', 'Loại hạn mức', 'Chi tiết hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Các loại khách hàng'): {
		'Thẻ Mastercard Ready': ('Số tiền tối đa/ngày', '100.000.000 VNĐ', 'Trên máy ATM', 'Chuyển tiền nhanh liên ngân hàng 24/7', 'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi'),
	},
	('Các loại khách hàng', 'Loại hạn mức', 'Chi tiết hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Tên thẻ'): {
		'Chủ thẻ >15 tuổi hạn mức thông thường': ('Số tiền tối đa/lần', '500.000.000 VNĐ', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready'),
		'Chủ thẻ >15 tuổi hạn mức cao': ('Số tiền tối đa/lần', '1.000.000.000 VNĐ', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready'),
		'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi': ('Số tiền tối đa/ngày', '5.000.000 VNĐ', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready'),
		'Chủ thẻ đủ 11 -  chưa đủ 15 tuổi': ('Số tiền tối đa/ngày', '100.000.000 VNĐ', 'Trên máy ATM', 'Chuyển tiền nhanh liên ngân hàng 24/7', 'Thẻ Mastercard Ready'),
	},
	('Loại hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Tên thẻ', 'Số lần giao dịch/ngày', 'Các loại khách hàng'): {
		'Số lần tối đa/ngày': ('Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', '20 lần', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
	},
	('Loại giao dịch', 'Loại hạn mức', 'Chi tiết giao dịch', 'Tên thẻ', 'Số lần giao dịch/ngày', 'Các loại khách hàng'): {
		'Trên máy ATM': ('Số lần tối đa/ngày', 'Chuyển khoản', 'Thẻ Mastercard Ready', '20 lần', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
		'Trên thiết bị chấp nhận thanh toán POS': ('Số lần tối đa/ngày', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', '20 lần', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
	},
	('Chi tiết giao dịch', 'Loại hạn mức', 'Loại giao dịch', 'Tên thẻ', 'Số lần giao dịch/ngày', 'Các loại khách hàng'): {
		'Rút tiền mặt bằng thẻ': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thẻ Mastercard Ready', '40 lần', 'Chủ thẻ >15 tuổi hạn mức thông thường'),
		'Chuyển khoản': ('Số lần tối đa/ngày', 'Trên máy ATM', 'Thẻ Mastercard Ready', '20 lần', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
		'Thanh toán hàng hóa dịch vụ': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thẻ Mastercard Ready', '20 lần', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
	},
	('Tên thẻ', 'Loại hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Số lần giao dịch/ngày', 'Các loại khách hàng'): {
		'Thẻ Mastercard Ready': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', '20 lần', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
	},
	('Số lần giao dịch/ngày', 'Loại hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Tên thẻ', 'Các loại khách hàng'): {
		'99 lần': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức cao'),
		'40 lần': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Rút tiền mặt bằng thẻ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức thông thường'),
		'20 lần': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi'),
		'30 lần': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', 'Chủ thẻ >15 tuổi hạn mức thông thường'),
	},
	('Các loại khách hàng', 'Loại hạn mức', 'Loại giao dịch', 'Chi tiết giao dịch', 'Tên thẻ', 'Số lần giao dịch/ngày'): {
		'Chủ thẻ >15 tuổi hạn mức cao': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', '99 lần'),
		'Chủ thẻ >15 tuổi hạn mức thông thường': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', '30 lần'),
		'Chủ thẻ đủ 6 -  chưa đủ 11 tuổi': ('Số lần tối đa/ngày', 'Trên thiết bị chấp nhận thanh toán POS', 'Thanh toán hàng hóa dịch vụ', 'Thẻ Mastercard Ready', '20 lần'),
	},
}