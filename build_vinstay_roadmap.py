import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border

def create_vinstay_roadmap():
    # Load base template
    template_path = 'src/CS13_Roadmap_De1.xlsx'
    wb = openpyxl.load_workbook(template_path)

    # -------------------------------------------------------------
    # 0_Hướng dẫn
    # -------------------------------------------------------------
    ws_guide = wb['0_Hướng dẫn']
    ws_guide['A1'] = "CS13 · Lộ trình sản phẩm AI 12 tháng — Dự án: Vinstay AI"
    ws_guide['A2'] = "Dự án riêng được giảng viên phê duyệt: Vinstay AI (Nền tảng thuê căn hộ & chốt cọc nhanh)."

    # -------------------------------------------------------------
    # 0_Đầu vào
    # -------------------------------------------------------------
    ws0 = wb['0_Đầu vào']
    ws0['A1'] = "0 · Nhiệm vụ 0: đọc bối cảnh & hồ sơ dự án Vinstay AI"
    for r in range(5, 11):
        ws0.cell(r, 2).value = "Có"
    
    ws0['E5'] = "Đã cấu hình thông số kinh tế thực tế của Vinstay AI vào dòng 12–20 trang 2 (Chi phí AI 650đ, hạ tầng 350đ, biên gộp > 60%)"
    ws0['E6'] = "Bối cảnh: Nền tảng Proptech kết nối Khách thuê, Chủ nhà, Host tại Vinhomes; đơn vị 1 việc là 1 lượt tìm kiếm & chốt cọc"
    ws0['E7'] = "6 việc trọng tâm: Cọc nhanh Fast Deposit, đối soát giá sàn, kiểm tra nội thất, chatbot tiện ích, điều phối Host, eKYC hợp đồng"
    ws0['E8'] = "Cổng chất lượng: Độ chính xác matching ≥ 98%, 0 vi phạm giá sàn chủ nhà, đối soát VietQR 100% trước khi tăng tự động hóa"
    ws0['E9'] = "Chuyên gia: Product Manager, Kỹ sư AI, Chuyên viên vận hành (Ops), Host Lead, Cố vấn pháp lý bất động sản"
    ws0['E10'] = "Người duyệt của công ty: Chuyên viên vận hành (Ops Lead) duyệt 25% ở Mức 1, giảm xuống 10% ở Mức 2 và 3% ở Mức 3"

    # -------------------------------------------------------------
    # 1_Danh sách việc
    # -------------------------------------------------------------
    ws1 = wb['1_Danh sách việc']
    items = [
        # B: Tên việc, C: Kết quả muốn đạt, D: Giả thuyết, E: Chỉ số & ngưỡng, F: Độ phủ, G: Tác động, H: Tự tin, I: Công sức, J: Dữ liệu, K: Đánh giá, L: Rủi ro nuốt, P: Quyết định, Q: Lý do
        (
            "Gợi ý căn hộ & tính toán gói cọc nhanh (Fast Deposit)",
            "Tăng 35% tỷ lệ chốt cọc nhanh không qua xem trực tiếp, giảm 60% thời gian tìm căn",
            "Ta tin rằng gợi ý căn hộ chuẩn xác kèm ưu đãi cọc nhanh (giữ căn 24h qua VietQR) cho khách thuê sẽ giúp tăng tỷ lệ chốt cọc giữ chỗ lên ≥ 25% ngay trong 24 giờ đầu.",
            "Tỷ lệ khách bấm chốt cọc nhanh đạt ≥ 20% trên tổng lượt xem căn; thời gian từ tìm kiếm đến cọc giảm từ 5 ngày xuống dưới 24 giờ.",
            5, 5, 0.8, 2, 0.8, 0.7, 0.2,
            "Tự làm",
            "Tính năng tạo doanh thu cọc trực tiếp và là lợi thế cạnh tranh cốt lõi của Vinstay."
        ),
        (
            "Đối soát chiết khấu chu kỳ thanh toán & giá sàn",
            "100% hợp đồng ký không vi phạm giá sàn chủ nhà, giảm 70% thời gian thương lượng giá",
            "Ta tin rằng tự động tính toán chiết khấu tiền thuê linh hoạt (1, 3, 6 tháng) mà luôn giữ trên mức giá sàn cho khách thuê sẽ giúp tăng tỷ lệ ký hợp đồng kỳ hạn dài thêm 30%.",
            "0 lỗi vi phạm giá sàn trên 100% hợp đồng; tỷ lệ chọn chu kỳ thanh toán ≥ 3 tháng đạt ≥ 45%.",
            4, 4, 0.8, 1, 0.9, 0.9, 0.1,
            "Tự làm",
            "Dữ liệu và logic toán học đã sẵn sàng 100%, bảo vệ quyền lợi sống còn của chủ nhà."
        ),
        (
            "Kiểm tra hiện trạng nội thất qua ảnh (AI Inspection)",
            "Giảm 50% thời gian bàn giao căn hộ, phát hiện 95% sai lệch đồ đạc nội thất",
            "Ta tin rằng đối chiếu ảnh hiện trạng bàn giao với danh mục đồ đạc ký gửi (Consign Wizard) cho Host và Khách thuê sẽ giúp giảm 80% tranh chấp hao mòn đồ đạc khi thanh lý hợp đồng.",
            "Độ chính xác nhận diện nội thất ≥ 92% trên bộ test 150 phòng; tỷ lệ khiếu nại bàn giao giảm xuống dưới 3%.",
            4, 4, 0.5, 3, 0.6, 0.5, 0.4,
            "Chờ",
            "Chờ sau 3 tháng để thu thập đủ 300 bộ ảnh bàn giao thực tế; hiện tại tập trung dòng tiền từ cọc."
        ),
        (
            "Chatbot tư vấn tiện ích & nội quy tòa nhà",
            "Giảm 70% cuộc gọi hỏi đáp phí quản lý, chỗ gửi xe, quy định thú cưng",
            "Ta tin rằng việc AI tự động trả lời 24/7 các câu hỏi về tiện ích, chi phí quản lý cho khách thuê sẽ giúp giải phóng 60% thời gian trực hotline của đội Host.",
            "Tỷ lệ trả lời chính xác thông tin nội quy tòa nhà ≥ 95% trên 100 câu hỏi mẫu; tỷ lệ hài lòng khách hàng ≥ 4,5/5,0 sao.",
            4, 3, 0.8, 2, 0.8, 0.7, 0.6,
            "Mua",
            "Tính năng phổ thông, tích hợp API chatbot/RAG có sẵn để tiết kiệm thời gian cho đội phát triển."
        ),
        (
            "Điều phối lịch xem nhà theo khu vực cho Host",
            "Giảm 40% thời gian di chuyển của Host, 100% khách được hỗ trợ trong 15 phút",
            "Ta tin rằng tự động phân bổ Host theo phân khu (Zone Scope) và lịch trống của Host khi khách muốn xem nhà trực tiếp sẽ giúp tỷ lệ Host nhận ca trong vòng 5 phút đạt ≥ 90%.",
            "Thời gian phản hồi điều phối Host < 10 phút; tỷ lệ hủy hẹn xem phòng giảm từ 25% xuống dưới 8%.",
            3, 3, 0.8, 2, 0.7, 0.8, 0.1,
            "Tự làm",
            "Đưa vào lộ trình giai đoạn Tiếp theo (3–6 tháng) sau khi mạng lưới Host mở rộng trên 30 người."
        ),
        (
            "Soạn thảo hợp đồng thuê tự động & eKYC",
            "100% hợp đồng tạo tự động không sai sót pháp lý, rút ngắn thời gian ký còn 5 phút",
            "Ta tin rằng trích xuất tự động thông tin căn hộ, điều khoản cọc, thông tin CCCD vào mẫu hợp đồng chuẩn cho khách và chủ nhà ký số sẽ giúp giảm 90% thời gian soạn hợp đồng thủ công.",
            "0 lỗi sai thông tin pháp lý trên 100 hợp đồng thử nghiệm; 100% đối chiếu CCCD hợp lệ trước khi ký.",
            4, 4, 0.8, 2, 0.9, 0.8, 0.2,
            "Tự làm",
            "Triển khai song hành cùng luồng chốt cọc để khép kín chu trình giao dịch trực tuyến."
        )
    ]

    for idx, item in enumerate(items):
        row = 5 + idx
        ws1.cell(row, 2).value = item[0]  # B
        ws1.cell(row, 3).value = item[1]  # C
        ws1.cell(row, 4).value = item[2]  # D
        ws1.cell(row, 5).value = item[3]  # E
        ws1.cell(row, 6).value = item[4]  # F
        ws1.cell(row, 7).value = item[5]  # G
        ws1.cell(row, 8).value = item[6]  # H
        ws1.cell(row, 9).value = item[7]  # I
        ws1.cell(row, 10).value = item[8] # J
        ws1.cell(row, 11).value = item[9] # K
        ws1.cell(row, 12).value = item[10]# L
        ws1.cell(row, 16).value = item[11]# P
        ws1.cell(row, 17).value = item[12]# Q

    # -------------------------------------------------------------
    # 2_Mức tự động
    # -------------------------------------------------------------
    ws2 = wb['2_Mức tự động']
    # Economic inputs
    ws2['B12'] = 650
    ws2['C12'] = "Chi phí token gọi LLM OpenAI/Claude trích xuất nhu cầu, filter căn và tính cọc; tính 10% retry"
    ws2['B13'] = 350
    ws2['C13'] = "Hạ tầng serverless, database vector, webhook VietQR, logging nhật ký"
    ws2['B14'] = 2.5
    ws2['C14'] = "Thời gian chuyên viên Ops kiểm tra thông tin căn, đối soát thanh toán cọc và giá sàn"
    ws2['B15'] = 80000
    ws2['C15'] = "Chi phí 1 giờ chuyên viên vận hành / CSKH của Vinstay"
    ws2['B16'] = 4500000
    ws2['C16'] = "Phí dịch vụ/hoa hồng quản lý giỏ hàng căn hộ bình quân mỗi tháng"
    ws2['B17'] = 1200
    ws2['C17'] = "Số lượt tìm kiếm, tư vấn và xử lý cọc bình quân mỗi tháng"
    ws2['B18'] = "Doanh thu bình quân (60% doanh thu đến từ 20% giỏ hàng căn hộ cao cấp và chu kỳ mùa tựu trường)"
    ws2['C18'] = "Rủi ro lệch mùa vụ và tỷ lệ lấp đầy căn hộ"
    ws2['B19'] = "NẾU doanh thu bình quân dưới 3,2 triệu/khách trong 2 tháng liên tiếp, trên ít nhất 15 đối tác, THÌ dừng mở rộng vùng mới"
    ws2['C19'] = "Ngưỡng an toàn bảo vệ dòng tiền hoạt động"
    ws2['B20'] = 8
    ws2['C20'] = "Kịch bản xấu: các chủ nhà/đối tác ký chậm 4 tháng sau thử nghiệm"
    ws2['A22'] = "Ghi chú: Người duyệt là chuyên viên vận hành (Ops) của Vinstay. Tỷ lệ duyệt: Mức 1 duyệt 25%, Mức 2 duyệt 10%, Mức 3 duyệt 3%."

    # Level 0
    ws2['C5'] = "AI gợi ý top 3 căn hộ phù hợp nhu cầu và tính toán số tiền cọc nhanh chiết khấu."
    ws2['D5'] = "Chuyên viên Ops / Host kiểm tra 100% thông tin và giá cọc trước khi gửi cho khách."
    ws2['E5'] = "— (mức khởi đầu)"
    ws2['F5'] = "Database 500 căn hộ Vinhomes; tích hợp cổng VietQR tạo mã tĩnh."
    ws2['G5'] = "T1–T2"
    ws2['H5'] = 1.0
    ws2['I5'] = "Người của mình"

    # Level 1
    ws2['C6'] = "AI tự động gửi đề xuất cọc nhanh kèm mã VietQR động; khóa tạm thời unit holding 30 phút."
    ws2['D6'] = "Chuyên viên Ops duyệt mẫu 25% các ca cọc giá trị cao hoặc ca khách yêu cầu hỗ trợ đặc biệt."
    ws2['E6'] = "Độ chính xác matching và tính cọc ≥ 98% trên bộ test 120 ca; 0 lỗi vi phạm giá sàn chủ nhà, do Ops Lead xác nhận."
    ws2['F6'] = "Bộ đề chuẩn 120 tình huống; webhook ngân hàng báo có tự động; quy chế bảo mật thông tin."
    ws2['G6'] = "T2–T3"
    ws2['H6'] = 0.25
    ws2['I6'] = "Người của mình"

    # Level 2
    ws2['C7'] = "AI tự động chốt cọc nhanh và khóa giữ căn 24h đối với 90% căn hộ tiêu chuẩn."
    ws2['D7'] = "Chuyên viên Ops chỉ can thiệp xử lý 10% các ca vi phạm ranh giới giá sàn hoặc tranh chấp lịch giữ chỗ."
    ws2['E7'] = "Tỷ lệ chốt cọc thành công không khiếu nại ≥ 95% trên ≥ 300 giao dịch cọc thực tế; tỷ lệ hủy cọc ≤ 5%, do Giám đốc Sản phẩm duyệt."
    ws2['F7'] = "Hàng chờ duyệt tự động (dispatch queue); module giải quyết khiếu nại tự động; tích hợp smartlock."
    ws2['G7'] = "T4–T6"
    ws2['H7'] = 0.10
    ws2['I7'] = "Người của mình"

    # Level 3
    ws2['C8'] = "AI tự động toàn trình: gợi ý căn, nhận cọc VietQR, kích hoạt hợp đồng điện tử và cấp mã mở cửa phòng."
    ws2['D8'] = "Đội ngũ vận hành theo dõi bảng giám sát thời gian thực, can thiệp 3% ca ngoại lệ phát sinh sự cố."
    ws2['E8'] = "Độ chính xác thanh toán và eKYC đạt 100% trên ≥ 500 hợp đồng; tỷ lệ người duyệt can thiệp < 3%, do CTO và Trưởng ban Pháp chế duyệt."
    ws2['F8'] = "Tích hợp cơ sở dữ liệu dân cư CCCD/eKYC; hợp đồng điện tử ký số; hệ sinh thái smartlock toàn khu."
    ws2['G8'] = "T7+"
    ws2['H8'] = 0.03
    ws2['I8'] = "Người của mình"

    # -------------------------------------------------------------
    # 3_Bảng lộ trình
    # -------------------------------------------------------------
    ws3 = wb['3_Bảng lộ trình']
    
    # Bây giờ (0–3 tháng) - B5:B12
    ws3['B5'] = "Đối soát chiết khấu chu kỳ thanh toán & giá sàn (Hạng 1) kết hợp Gợi ý căn hộ & chốt cọc nhanh Fast Deposit (Hạng 2)."
    ws3['B6'] = "Gợi ý căn hộ chuẩn xác kèm ưu đãi cọc nhanh (giảm cọc 450.000đ giữ chỗ 24h qua VietQR) giúp khách chốt cọc ngay mà không cần chờ xem nhà trực tiếp."
    ws3['B7'] = "Tỷ lệ chốt cọc nhanh đạt ≥ 20% trên tổng lượt xem căn; 0 lỗi vi phạm giá sàn chủ nhà trên 100% giao dịch; thời gian chốt cọc giảm từ 5 ngày xuống dưới 24 giờ."
    ws3['B8'] = "Triển khai Mức 0 (gợi ý có duyệt) trong tháng 1, sau đó vượt cổng chuyển lên Mức 1 (hỗ trợ có duyệt, người duyệt 25% ca) trong tháng 2–3."
    ws3['B9'] = "Bộ đề 120 tình huống: độ chính xác matching ≥ 98%, 0 lỗi vi phạm giá sàn, tỷ lệ Ops phải sửa đề xuất < 10% trước khi mở rộng lên Mức 1."
    ws3['B10'] = "Tích hợp giỏ hàng 500 căn Vinhomes cập nhật trạng thái thời gian thực; webhook thanh toán VietQR tự động báo có; quy chế bảo vệ dữ liệu khách thuê."
    ws3['B11'] = "Chi phí AI 650đ/việc, hạ tầng 350đ/việc; Mức 1 duyệt 25% đạt biên gộp 51,1%, chuẩn bị lên Mức 2 đạt 64,4% (>60%); doanh thu bình quân 4,5 triệu/tháng/1.200 việc."
    ws3['B12'] = "NẾU doanh thu bình quân dưới 3,2 triệu đồng/khách trong 2 tháng liên tiếp, hoặc tỷ lệ khiếu nại cọc vượt quá 5% trên ít nhất 200 lượt cọc, THÌ dừng mở rộng phân khu mới và lùi về Mức 0."

    # Tiếp theo (3–6 tháng) - C5:C12
    ws3['C5'] = "Mở rộng tính năng Tự động điều phối lịch xem nhà theo khu vực cho Host (Hạng 4) và nâng cấp lên Mức tự động 2 (Tự động một phần)."
    ws3['C6'] = "Tự động phân bổ ca cho Host gần nhất giúp giảm thời gian chờ của khách và tăng tỷ lệ tiếp cận khách thêm 40%."
    ws3['C7'] = "Thời gian Host nhận ca < 5 phút; tỷ lệ chốt thành công sau xem nhà đạt ≥ 35%; biên lợi nhuận gộp toàn hệ thống đạt ≥ 64,4%."
    ws3['C8'] = "Mức 2 (Tự động một phần, tỷ lệ người duyệt giảm xuống 10%)."
    ws3['C9'] = "Đạt tỷ lệ hài lòng khách hàng ≥ 95% trên ≥ 300 giao dịch cọc thực tế; tỷ lệ hủy cọc ≤ 5%."
    ws3['C10'] = "Hệ thống định vị phân khu (Zone Scope) cho 50 Host; ứng dụng mobile cho Host nhận ca và báo cáo hiện trạng."
    ws3['C11'] = "Biên lợi nhuận gộp đạt 64,4% (vượt ngưỡng 60% của công ty), chi phí mỗi việc giảm còn 1.333 đồng."
    ws3['C12'] = "NẾU tỷ lệ Host từ chối nhận ca > 25% trong 3 tuần liên tiếp, THÌ dừng cơ chế điều phối tự động và quay lại phân bổ thủ công qua quản lý nhóm."

    # Sau này (6–12 tháng) - D5:D12
    ws3['D5'] = "Triển khai Tự động hóa hợp đồng điện tử & eKYC (Hạng 3) và Kiểm tra hiện trạng nội thất qua ảnh (Hạng 6); tiến tới Mức tự động 3."
    ws3['D6'] = "Khép kín toàn trình số hóa từ tìm căn, đặt cọc, ký hợp đồng đến nhận bàn giao giúp khách thuê chuyển vào ở ngay trong 2 giờ."
    ws3['D7'] = "100% hợp đồng ký điện tử có eKYC hợp lệ; thời gian xử lý hồ sơ < 15 phút; tỷ lệ người duyệt can thiệp < 3%."
    ws3['D8'] = "Mức 3 (Tự động có giám sát, người duyệt 3% ca ngoại lệ)."
    ws3['D9'] = "Kiểm thử 500 hợp đồng: 0 lỗi pháp lý, đối soát VietQR khớp 100%, tỷ lệ tranh chấp nội thất < 2%."
    ws3['D10'] = "Tích hợp cơ sở dữ liệu dân cư CCCD/eKYC; hợp đồng điện tử ký số; mô hình AI Vision phân tích ảnh nội thất."
    ws3['D11'] = "Biên lợi nhuận gộp tối ưu đạt 70,7%; doanh thu mở rộng đạt 6,5 triệu đồng/khách/tháng trên 2.000 việc."
    ws3['D12'] = "NẾU phát sinh 1 lỗi pháp lý nghiêm trọng về hợp đồng hoặc tranh chấp cọc không thể hòa giải, THÌ dừng ngay Mức 3 và kích hoạt kiểm toán toàn bộ quy trình."

    # -------------------------------------------------------------
    # 4_Rà soát
    # -------------------------------------------------------------
    ws4 = wb['4_Rà soát']
    ws4['B5'] = "Tỷ lệ khách bấm cọc nhanh Fast Deposit; tỷ lệ matching đúng căn hộ; tỷ lệ Ops phải sửa gợi ý"
    ws4['C5'] = "Đi tiếp nếu tỷ lệ sửa < 10%; Sửa lại prompt và bộ lọc căn hộ nếu tỷ lệ khách bỏ qua gợi ý > 40%"
    ws4['D5'] = "Quản lý sản phẩm (Product Manager) + Trưởng nhóm Vận hành (Ops Lead)"

    ws4['B6'] = "Cổng đánh giá chuyển giao từ Mức 0 lên Mức 1 (độ chính xác ≥ 98% trên 120 ca; 0 lỗi vi phạm giá sàn); biên lợi nhuận gộp"
    ws4['C6'] = "Đi tiếp (chính thức lên Mức 1) nếu đạt cổng; Sửa bộ quy tắc chiết khấu nếu có ca tiệm cận giá sàn nguy hiểm"
    ws4['D6'] = "Quản lý sản phẩm + Kế toán trưởng / Tài chính"

    ws4['B7'] = "Doanh thu bình quân mỗi khách so với ngưỡng dừng 3,2 triệu; tỷ lệ chuyển đổi ký hợp đồng thuê; dòng tiền hoạt động"
    ws4['C7'] = "Đi tiếp (chuẩn bị mở rộng sang phân khu mới và lên Mức 2) / Đổi hướng nếu doanh thu bình quân không tăng trưởng"
    ws4['D7'] = "Ban Giám đốc (CEO/COO) + Quản lý sản phẩm"

    ws4['B8'] = "Chi phí token gọi AI (hiện tại 650đ); độ trễ phản hồi (latency); khả năng hiểu ngữ cảnh tìm kiếm tiếng Việt"
    ws4['C8'] = "Chạy lại bộ đề chuẩn 120 ca; nếu đạt chất lượng tương đương, chuyển sang mô hình mới để nâng biên lợi nhuận gộp"
    ws4['D8'] = "Kỹ sư trưởng AI (AI Tech Lead) + Quản lý sản phẩm"

    ws4['B9'] = "Đối thủ lớn (Batdongsan, Chợ Tốt) hoặc mạng xã hội ra tính năng cọc trực tuyến / bot tìm phòng"
    ws4['C9'] = "Bỏ các tính năng hỏi đáp thông thường bị sao chép; dồn toàn lực vào tính năng độc quyền: giỏ hàng độc quyền, cọc nhanh VietQR và mạng lưới Host tại chỗ"
    ws4['D9'] = "Ban Giám đốc (CEO/COO)"

    ws4['B10'] = "Luật Kinh doanh Bất động sản mới về đặt cọc, giao dịch điện tử và bảo vệ dữ liệu cá nhân (Nghị định 13)"
    ws4['C10'] = "Điều chỉnh hợp đồng mẫu, cập nhật giới hạn tỷ lệ cọc tối đa (0.5x - 4.0x rent) và quy trình lưu trữ CCCD/eKYC"
    ws4['D10'] = "Trưởng ban Pháp chế + Quản lý sản phẩm"

    # -------------------------------------------------------------
    # 5_Slide lãnh đạo (≤ 60 từ mỗi ô)
    # -------------------------------------------------------------
    ws5 = wb['5_Slide lãnh đạo']
    ws5['B4'] = "Tập trung 3 tháng đầu vào tính năng Chốt cọc nhanh (Fast Deposit) và kiểm soát giá sàn, đưa sản phẩm từ Mức 0 lên Mức 1 với biên lợi nhuận trên 51%, trước khi mở rộng mạng lưới Host."
    ws5['B5'] = "Bây giờ: Tự động hóa gợi ý cọc nhanh và đối soát giá sàn (Mức 1). Tiếp theo: Điều phối Host theo phân khu (Mức 2). Sau này: Hợp đồng số eKYC và kiểm định nội thất qua ảnh (Mức 3)."
    ws5['B6'] = "2 kỹ sư phần mềm, 1 kỹ sư AI, 1 chuyên viên vận hành; ngân sách AI và hạ tầng 1.000 đồng/việc; kết nối giỏ hàng 500 căn hộ Vinhomes và cổng thanh toán VietQR."
    ws5['B7'] = "Khách thuê ngại cọc không xem phòng hoặc vi phạm giá sàn chủ nhà. Xử lý: Cam kết hoàn cọc nếu căn không đúng ảnh, khóa chặn cứng giá sàn và duy trì người duyệt 25% ca."
    ws5['B8'] = "Rà soát định kỳ vào ngày 30, 60, 90; kích hoạt xem xét khẩn cấp nếu doanh thu bình quân dưới 3,2 triệu trong 2 tháng liên tiếp hoặc khi xuất hiện mô hình AI rẻ hơn."

    # -------------------------------------------------------------
    # 7_Thang điểm
    # -------------------------------------------------------------
    ws7 = wb['7_Thang điểm']
    ws7['D5'] = 20
    ws7['D6'] = 20
    ws7['D7'] = 25
    ws7['D8'] = 15
    ws7['D9'] = 20

    # Save to final project file
    output_file = 'Vinstay_CS13.xlsx'
    wb.save(output_file)
    print(f"Created {output_file} successfully!")

if __name__ == '__main__':
    create_vinstay_roadmap()
