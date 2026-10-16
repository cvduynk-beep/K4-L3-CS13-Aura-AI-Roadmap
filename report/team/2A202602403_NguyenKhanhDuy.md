# Báo cáo cá nhân — Nguyễn Khánh Duy

## 1. Thông tin thành viên
- **Họ và tên**: Nguyễn Khánh Duy
- **MSSV**: 2A202602403
- **Nhóm**: Team Vinstay
- **Đề tài**: Dự án riêng — Vinstay AI (Trợ lý thông minh thuê căn hộ & Chốt cọc nhanh)
- **Vai trò trong nhóm**: Trưởng nhóm / Product Lead (Định hướng sản phẩm, Giả thuyết & Báo cáo Lãnh đạo)

---

## 2. Phần việc phụ trách chính
- **Nhiệm vụ 0 & 1 (CP1) — Đọc hồ sơ, xác lập bối cảnh & Xây dựng Giả thuyết sản phẩm**:
  - Khởi tạo dự án, thiết lập sheet `0_Đầu vào` xác nhận 6 mục nền tảng.
  - Định nghĩa "1 việc" của Vinstay AI: *1 lượt khách tìm kiếm, nhận tư vấn và tiến hành chốt cọc trực tuyến*.
  - Xây dựng 6 giả thuyết tính năng trọng tâm theo khung chuẩn: *"Ta tin rằng làm [X] cho đối tượng [Y] sẽ giúp đạt [Z]"* và gán chỉ số đo lường kèm con số cụ thể tại sheet `1_Danh sách việc` (Cột B–E).
- **Nhiệm vụ 5 (CP5) — Xây dựng nội dung Slide Lãnh đạo**:
  - Soạn thảo 5 khối nội dung cô đọng tại sheet `5_Slide lãnh đạo` (B4:B8, độ dài chuẩn 35–41 từ, không vượt quá 60 từ).
  - Thiết kế cấu trúc 1 slide trực quan, ngắn gọn, đưa kết luận lên đầu (Bottom Line Up Front) cho Ban Lãnh đạo.
- **Quản trị chung & Đảm bảo chất lượng (QA)**:
  - Khởi tạo GitHub repo nhóm, phân công nhiệm vụ, kết nối các phần việc của thành viên.
  - Rà soát sheet `6_Tự kiểm tra` đạt tuyệt đối 8/8 mục `Đạt` và chuẩn bị hồ sơ nộp bài trên VLearn.

---

## 3. Đóng góp cụ thể & Quyết định sản phẩm
1. **Chiến lược sản phẩm & Xác lập Giả thuyết**:
   - Định vị giá trị cốt lõi (Core Value Proposition) của Vinstay AI là **rút ngắn thời gian từ lúc tìm kiếm đến lúc chốt cọc** từ 5 ngày xuống dưới 24 giờ thông qua tính năng *Chốt cọc nhanh (Fast Deposit)*.
   - Thiết lập chỉ số thành công đo lường được: Tỷ lệ khách bấm cọc nhanh đạt $\ge 20\%$ trên tổng số lượt xem căn; 0 lỗi vi phạm giá sàn của chủ nhà; thời gian ký hợp đồng rút ngắn còn 5 phút.
   - Thống nhất cùng nhóm ưu tiên làm trước 2 tính năng: *Đối soát chiết khấu chu kỳ thanh toán & giá sàn* (Hạng 1) và *Gợi ý căn hộ & chốt cọc nhanh* (Hạng 2).
2. **Soạn thảo Slide Lãnh đạo (Bottom Line Up Front)**:
   - Đưa kết luận chiến lược lên đầu: *Tập trung 3 tháng đầu vào tính năng Chốt cọc nhanh và kiểm soát giá sàn, đưa sản phẩm từ Mức 0 lên Mức 1 với biên lợi nhuận trên 51%, trước khi mở rộng mạng lưới Host*.
   - Khái quát 3 việc chính theo 3 tầng (Bây giờ / Tiếp theo / Sau này), làm rõ nguồn lực cần thiết (2 dev, 1 AI, 1 Ops, 1.000đ/việc) và cách quản trị rủi ro lớn nhất (cam kết hoàn cọc, khóa giá sàn, duy trì 25% người duyệt).

---

## 4. Bằng chứng đóng góp trong sản phẩm
- **File Excel `Vinstay_CS13.xlsx`**:
  - Sheet `0_Hướng dẫn` và `0_Đầu vào`: Toàn bộ các ô $B5:B10$ và $E5:E10$.
  - Sheet `1_Danh sách việc`: Cột $B, C, D, E$ (Tên việc, kết quả, giả thuyết và chỉ số có số đo lường) từ dòng 5–10; cột $O$ báo `Có` 100%.
  - Sheet `5_Slide lãnh đạo`: Các ô $B4:B8$ (đều báo `Đạt` ở cột $D$).
  - Sheet `6_Tự kiểm tra`: Kiểm soát 8/8 chỉ số báo `Đạt`.
  - Sheet `7_Thang điểm`: Tự đánh giá 100/100 điểm.
- **Tài liệu nộp bài**: File [SLIDE_LANH_DAO.md](../../SLIDE_LANH_DAO.md) và quản lý repo GitHub.

---

## 5. Tự đánh giá & Bài học rút ra
- **Điều hiểu rõ nhất**: Cách chuyển đổi các ý tưởng tính năng thành giả thuyết có thể đo lường và kiểm chứng, thay vì chỉ lập danh sách tính năng mơ hồ.
- **Giả định cần kiểm chứng thêm**: Khả năng chấp nhận cọc nhanh của tệp khách hàng phân khúc căn hộ giá rẻ (Studio/1PN) so với căn hộ gia đình (2PN/3PN); cần phân tích A/B testing theo từng loại hình căn hộ trong 30 ngày đầu.
