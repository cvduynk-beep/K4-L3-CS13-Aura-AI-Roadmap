# Báo cáo cá nhân — Cao Đức Hiệp

## 1. Thông tin thành viên
- **Họ và tên**: Cao Đức Hiệp
- **MSSV**: 2A202602550
- **Nhóm**: Team Vinstay
- **Đề tài**: Dự án riêng — Vinstay AI (Trợ lý thông minh thuê căn hộ & Chốt cọc nhanh)
- **Vai trò trong nhóm**: Operations & Finance Lead (Mô hình kinh tế, Vận hành & Lộ trình rà soát)

---

## 2. Phần việc phụ trách chính
- **Nhiệm vụ 3 (CP3) — Xây dựng mô hình kinh tế Unit Economics & Biên lợi nhuận gộp**:
  - Khảo sát và thiết lập các biến số kinh tế thực tế của Vinstay AI tại dòng 12–20 sheet `2_Mức tự động` (chi phí gọi API LLM, hạ tầng serverless, thời gian duyệt của Ops, lương chuyên viên, doanh thu bình quân và số việc mỗi tháng).
  - Tối ưu hóa tỷ lệ can thiệp của con người ($H$) theo từng mức để bảo đảm biên lợi nhuận gộp vượt ngưỡng yêu cầu $\ge 60\%$.
- **Nhiệm vụ 4 (CP4) — Lập Bảng lộ trình 3 tầng & Thiết lập Điều kiện dừng đo lường được**:
  - Hoàn thiện 8/8 dòng tầng Bây giờ (0–3 tháng), định hướng tầng Tiếp theo (3–6 tháng) và Sau này (6–12 tháng) tại sheet `3_Bảng lộ trình`.
  - Thiết kế điều kiện dừng (Kill condition) cụ thể bằng con số nhằm bảo vệ an toàn dòng tiền của startup.
- **Nhiệm vụ 4 (CP4) — Lịch rà soát kinh doanh & Tuân thủ pháp lý**:
  - Thiết lập cơ chế rà soát định kỳ Ngày 30, Ngày 60, Ngày 90 và kế hoạch ứng phó khi thay đổi chính sách pháp luật tại sheet `4_Rà soát`.

---

## 3. Đóng góp cụ thể & Tính toán kinh tế
1. **Mô hình Unit Economics & Biên lợi nhuận gộp**:
   - Xác lập chi phí trực tiếp trên mỗi lượt giao dịch (1 việc):
     + Chi phí gọi AI ($B12$): `650 đồng` (OpenAI/Claude API kèm 10% retry).
     + Hạ tầng, database vector, webhook VietQR ($B13$): `350 đồng`.
     + Thời gian duyệt của Ops ($B14$): `2.5 phút/việc`; chi phí lương Ops ($B15$): `80.000 đồng/giờ` $\rightarrow$ Chi phí duyệt = $3.333$ đồng/lượt nếu duyệt 100%.
     + Doanh thu bình quân mỗi căn/khách ($B16$): `4.500.000 đồng/tháng` trên $1.200$ lượt giao dịch ($B17$).
   - Kết quả biên lợi nhuận gộp:
     + Mức 0 (Duyệt 100%): $-15.6\%$ (chấp nhận lỗ giai đoạn đầu để huấn luyện hệ thống).
     + Mức 1 (Duyệt 25%): $+51.1\%$.
     + Mức 2 (Duyệt 10%): $+64.4\%$ (**Đạt chuẩn $\ge 60\%$ của đề bài**).
     + Mức 3 (Duyệt 3%): $+70.7\%$.
2. **Xác lập Điều kiện dừng (Kill Condition) & Quản trị rủi ro**:
   - Nhận định biến số nguy hiểm nhất là sự sụt giảm doanh thu bình quân do tính mùa vụ (mùa tựu trường/chuyển việc).
   - Thiết lập điều kiện dừng rõ ràng: *NẾU doanh thu bình quân dưới 3,2 triệu đồng/khách trong 2 tháng liên tiếp, hoặc tỷ lệ khiếu nại cọc vượt quá 5% trên ít nhất 200 lượt cọc, THÌ dừng mở rộng phân khu mới và lùi về Mức 0*.
   - Kịch bản xấu: Điểm hòa vốn/hết tiền ở tháng thứ 8 nếu đối tác ký kết chậm trễ.

---

## 4. Bằng chứng đóng góp trong sản phẩm
- **File Excel `Vinstay_CS13.xlsx`**:
  - Sheet `2_Mức tự động`: Cột $H, I, J, K, L$ và khối Số liệu kinh tế $B12:C20$.
  - Sheet `3_Bảng lộ trình`: Hoàn thiện tầng Bây giờ (cột $B$), tầng Tiếp theo (cột $C$) và Sau này (cột $D$); đặc biệt là dòng 10 (Điều kiện cần), dòng 11 (Căn cứ kinh tế), dòng 12 (Điều kiện dừng).
  - Sheet `4_Rà soát`: Dòng 5 (Ngày 30), Dòng 6 (Ngày 60), Dòng 7 (Ngày 90) và Dòng 10 (Thay đổi quy định pháp lý bất động sản/eKYC).
- **Slide lãnh đạo**: Đóng góp số liệu chi phí $1.000$đ/việc, ngưỡng doanh thu $3.2$ triệu và mốc rà soát tài chính.

---

## 5. Tự đánh giá & Bài học rút ra
- **Điều hiểu rõ nhất**: Mối liên hệ chặt chẽ giữa mức độ tự động hóa AI và biên lợi nhuận gộp. Nếu không giảm được tỷ lệ can thiệp của con người qua từng mức thì doanh nghiệp AI càng tăng quy mô sẽ càng lỗ.
- **Giả định cần kiểm chứng thêm**: Tỷ lệ khách hàng chịu thanh toán cọc nhanh trực tiếp qua VietQR đạt mục tiêu $\ge 20\%$ hay vẫn đòi hỏi có Host dẫn đi xem phòng thực tế; cần theo dõi sát chỉ số này tại mốc Ngày 30.
