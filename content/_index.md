---
title: "Workshop Template"
date: "2026-05-02"
weight: 1
chapter: false
---

## Nội dung

1. [Proposal](Proposal/) — Đề xuất dự án / ý tưởng
2. [Workshop](Workshop/) — Tài liệu workshop

## 👥 Team Members

<style>
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  margin-top: 30px;
  justify-items: center;
  padding: 20px;
}

.team-card {
  position: relative;
  width: 340px;
  background: linear-gradient(145deg, rgba(255,255,255,0.95) 0%, rgba(248,250,252,0.9) 100%);
  border-radius: 20px;
  padding: 30px 25px;
  text-align: center;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

.team-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--card-color);
  transition: height 0.3s ease;
}

.team-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.team-card:hover::before {
  height: 6px;
}

.team-avatar-container {
  position: relative;
  width: 140px;
  height: 140px;
  margin: 0 auto 20px;
}

.team-avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid var(--card-color);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
  transition: transform 0.3s ease;
}

.team-card:hover .team-avatar {
  transform: scale(1.05);
}

.team-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202e;
  margin: 15px 0 8px;
  letter-spacing: -0.5px;
}

.team-role {
  display: inline-block;
  padding: 6px 16px;
  background: var(--card-color);
  color: white;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 18px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.team-divider {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, transparent, var(--card-color), transparent);
  margin: 15px auto;
  border-radius: 2px;
}

.team-info {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 15px;
}

.team-info-item {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 0.85rem;
  color: #64748b;
  padding: 8px 12px;
  background: rgba(241,245,249,0.6);
  border-radius: 10px;
  transition: background 0.3s ease;
}

.team-info-item:hover {
  background: rgba(241,245,249,0.9);
}

.team-info-icon {
  font-size: 1rem;
}

/* Role-specific colors */
.team-card.leader { --card-color: #e74c3c; }
.team-card.data-engineer { --card-color: #f39c12; }
.team-card.ai-engineer { --card-color: #3498db; }
.team-card.backend-engineer { --card-color: #27ae60; }

/* Responsive */
@media (max-width: 768px) {
  .team-grid {
    grid-template-columns: 1fr;
    padding: 10px;
  }
  .team-card {
    width: 100%;
    max-width: 340px;
  }
}
</style>

<div class="team-grid">

<!-- Member 1 - Leader -->
<div class="team-card leader">
  <div class="team-avatar-container">
    <img src="/images/Team/SE180011.JPG?v=2" alt="Triệu Quốc Hào" class="team-avatar">
  </div>
  <h3 class="team-name">Triệu Quốc Hào</h3>
  <span class="team-role">👑 Leader - Data Scientist</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>haotqse180011@fpt.edu.vn</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>078-491-9197</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE180011</span>
    </div>
  </div>
</div>

<!-- Member 2 - Data Engineer -->
<div class="team-card data-engineer">
  <div class="team-avatar-container">
    <img src="/images/Team/SE194447.JPG?v=2" alt="Nguyễn Quách Lam Giang" class="team-avatar">
  </div>
  <h3 class="team-name">Nguyễn Quách Lam Giang</h3>
  <span class="team-role">📊 Data Engineer</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>nguyenlamgiang2198@gmail.com</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>089-9197-017</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE194447</span>
    </div>
  </div>
</div>

<!-- Member 3 - AI Engineer -->
<div class="team-card ai-engineer">
  <div class="team-avatar-container">
    <img src="/images/Team/SE181823.JPG?v=2" alt="Nguyễn Văn Anh Duy" class="team-avatar">
  </div>
  <h3 class="team-name">Nguyễn Văn Anh Duy</h3>
  <span class="team-role">🤖 AI Engineer</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>duynguyenvananh@gmail.com</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>038-788-3041</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE181823</span>
    </div>
  </div>
</div>

<!-- Member 4 - AI Engineer -->
<div class="team-card ai-engineer">
  <div class="team-avatar-container">
    <img src="/images/Team/SE193028.JPG?v=2" alt="Trần Huỳnh Bảo Minh" class="team-avatar" style="object-position: center top;">
  </div>
  <h3 class="team-name">Trần Huỳnh Bảo Minh</h3>
  <span class="team-role">🤖 AI Engineer</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>baominhbrthcs@gmail.com</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>078-222-4999</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE193028</span>
    </div>
  </div>
</div>

<!-- Member 5 - Backend Engineer -->
<div class="team-card backend-engineer">
  <div class="team-avatar-container">
    <img src="/images/Team/SE181951.JPG?v=2" alt="Lê Vũ Phương Hoà" class="team-avatar">
  </div>
  <h3 class="team-name">Lê Vũ Phương Hoà</h3>
  <span class="team-role">⚙️ Backend Engineer</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>hoalvpse181951@fpt.edu.vn</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>032-703-0024</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE181951</span>
    </div>
  </div>
</div>

<!-- Member 6 - Backend Engineer -->
<div class="team-card backend-engineer">
  <div class="team-avatar-container">
    <img src="/images/Team/SE182968.JPG?v=2" alt="Nguyễn Công Minh" class="team-avatar">
  </div>
  <h3 class="team-name">Nguyễn Công Minh</h3>
  <span class="team-role">⚙️ Backend Engineer</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>minhncse182968@fpt.edu.vn</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>036-240-1520</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE182968</span>
    </div>
  </div>
</div>

<!-- Member 7 - Backend Engineer -->
<div class="team-card backend-engineer">
  <div class="team-avatar-container">
    <img src="/images/Team/SE180168.png?v=2" alt="Nguyễn Văn Duy Khiêm" class="team-avatar">
  </div>
  <h3 class="team-name">Nguyễn Văn Duy Khiêm</h3>
  <span class="team-role">⚙️ Backend Engineer</span>
  <div class="team-divider"></div>
  <div class="team-info">
    <div class="team-info-item">
      <span class="team-info-icon">Email:</span>
      <span>khiemnguyen120216@gmail.com</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">Phone:</span>
      <span>083-6262-507</span>
    </div>
    <div class="team-info-item">
      <span class="team-info-icon">ID:</span>
      <span>SE180168</span>
    </div>
  </div>
</div>

</div>
