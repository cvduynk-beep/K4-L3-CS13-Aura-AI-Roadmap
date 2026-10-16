# Báo cáo cá nhân — Lê Thanh Tùng

## 1. Thông tin thành viên
- **Họ và tên**: Lê Thanh Tùng
- **MSSV**: 2A202602499
- **Nhóm**: Team Vinstay
- **Đề tài**: Dự án riêng — Vinstay AI (Trợ lý thông minh thuê căn hộ & Chốt cọc nhanh)
- **Vai trò trong nhóm**: AI Tech Lead (Kiến trúc mô hình & Đánh giá chất lượng AI)

---

## 2. Phần việc phụ trách chính
- **Nhiệm vụ 2 (CP2) — Đánh giá kỹ thuật & Chấm điểm ưu tiên RICE mở rộng**:
  - Phụ trách đánh giá các chỉ số kỹ thuật: Mức tự tin ($H$), Độ sẵn sàng dữ liệu ($J$), Độ sẵn sàng đánh giá kiểm thử ($K$), và Rủi ro bị mô hình nền tảng/nền tảng lớn làm thay ($L$).
  - Ra quyết định kỹ thuật: `Tự làm`, `Mua`, hoặc `Chờ` cho từng tính năng tại sheet `1_Danh sách việc`.
- **Nhiệm vụ 3 (CP3) — Thiết lập 4 Cấp độ Tự động hóa & Cổng đánh giá (Evaluation Gate)**:
  - Phân định rõ trách nhiệm giữa AI và con người (Host/Ops) từ Mức 0 đến Mức 3.
  - Thiết lập cổng kiểm thử định lượng bắt buộc (chỉ số + ngưỡng + cỡ mẫu + người duyệt) trước khi cho phép AI nâng quyền tự động hóa tại sheet `2_Mức tự động`.
- **Nhiệm vụ 4 (CP4) — Kế hoạch rà soát khi có biến động công nghệ**:
  - Xây dựng phương án ứng phó kỹ thuật khi có mô hình AI mới ra mắt, giá token giảm mạnh hoặc đối thủ ra tính năng cạnh tranh tại sheet `4_Rà soát`.

---

## 3. Đóng góp cụ thể & Quyết định kỹ thuật
1. **Phân tích Rủi ro nền tảng (Platform Risk)**:
   - Nhận định tính năng *Chatbot tư vấn tiện ích & nội quy tòa nhà* có rủi ro bị nuốt cao ($L = 0.6$) vì các mô hình RAG mã nguồn mở/GPT store rất dễ sao chép $\rightarrow$ Đề xuất quyết định `Mua` (tận dụng giải pháp có sẵn) để không lãng phí tài nguyên dev.
   - Nhận định tính năng *Chốt cọc nhanh (Fast Deposit)* và *Đối soát giá sàn* có rủi ro bị nuốt rất thấp ($L = 0.1 - 0.2$) do gắn liền với giỏ hàng căn hộ độc quyền và luồng thanh toán VietQR ngân hàng $\rightarrow$ Quyết định `Tự làm` và ưu tiên số 1.
   - Tính năng *AI Vision kiểm định nội thất*: Do dữ liệu ảnh thực tế chưa đủ chuẩn ($J = 0.6, K = 0.5$) $\rightarrow$ Đề xuất quyết định `Chờ` sau 3 tháng để tránh triển khai vội vàng gây sai sót.
2. **Thiết lập Cổng đánh giá (Evaluation Gate) định lượng**:
   - **Cổng lên Mức 1**: Bộ đề test 120 ca thực tế; độ chính xác matching $\ge 98\%$, 0 lỗi vi phạm giá sàn chủ nhà, Ops Lead xác nhận.
   - **Cổng lên Mức 2**: Thử nghiệm trên $\ge 300$ giao dịch cọc thật; tỷ lệ cọc thành công không khiếu nại $\ge 95\%$, tỷ lệ hủy cọc $\le 5\%$, Giám đốc Sản phẩm duyệt.
   - **Cổng lên Mức 3**: Kiểm thử $\ge 500$ hợp đồng; độ chính xác thanh toán và eKYC đạt 100%, tỷ lệ can thiệp con người $< 3\%$, CTO và Pháp chế duyệt.

---

## 4. Bằng chứng đóng góp trong sản phẩm
- **File Excel `Vinstay_CS13.xlsx`**:
  - Sheet `1_Danh sách việc`: Toàn bộ cột kỹ thuật $F, G, H, I, J, K, L$, cột quyết định $P$ và lý do kỹ thuật $Q$ (dòng 5–10).
  - Sheet `2_Mức tự động`: Cột $C, D, E, F, G$ cho Mức 0 đến Mức 3; cột $M$ báo `Có` cho 3 cổng đánh giá định lượng.
  - Sheet `4_Rà soát`: Dòng 8 (khi có model mới/giá token giảm) và Dòng 9 (đối thủ ra tính năng đè).
- **Slide lãnh đạo**: Đóng góp nội dung khối *Khắc phục rủi ro kỹ thuật* và *Cổng đánh giá chuyển mức*.

---

## 5. Tự đánh giá & Bài học rút ra
- **Điều hiểu rõ nhất**: Cách áp dụng công thức RICE mở rộng có tính đến hệ số sẵn sàng dữ liệu và rủi ro bị nền tảng "nuốt" để chọn đúng tính năng tạo ra hào lũy công nghệ (moat) cho startup thay vì làm những tính năng AI chung chung.
- **Giả định cần kiểm chứng thêm**: Khả năng phân tích ảnh hiện trạng nội thất (AI Inspection) trong điều kiện ánh sáng yếu tại các căn hộ thực tế; cần kiểm chứng trên tập dữ liệu ảnh thu thập trong 90 ngày đầu.
