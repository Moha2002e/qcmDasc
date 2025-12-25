<script setup>
import chaptersData from '../data/chapters.json'

defineEmits(['select-chapter'])

const chapters = chaptersData
</script>

<template>
  <div class="menu-container">
    <h1 class="main-title">Modules de Cours</h1>
    <p class="subtitle">Sélectionnez un chapitre pour commencer le QCM</p>

    <div class="chapters-grid">
      <div 
        v-for="chapter in chapters" 
        :key="chapter.id"
        class="chapter-card"
        :class="{ 'disabled': chapter.status === 'coming_soon' }"
        @click="chapter.status === 'active' && $emit('select-chapter', chapter.id)"
      >
        <div class="card-content">
          <div class="status-badge" :class="chapter.status">
            {{ chapter.status === 'active' ? 'Disponible' : 'Bientôt' }}
          </div>
          <h3>{{ chapter.title }}</h3>
          <p>{{ chapter.description }}</p>
          <div class="action-arrow">→</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.menu-container {
  width: 100%;
  max-width: 1200px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-title {
  font-size: 3rem;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #fff 0%, #a5f3fc 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-align: center;
}

@media (max-width: 768px) {
  .main-title {
    font-size: 2rem;
  }
  .menu-container {
    padding: 1rem;
  }
}

.subtitle {
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 3rem;
  font-size: 1.2rem;
  text-align: center;
}

.chapters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  width: 100%;
}

@media (max-width: 600px) {
  .chapters-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

.chapter-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 2rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.chapter-card:hover:not(.disabled) {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  border-color: rgba(255, 255, 255, 0.3);
}

.chapter-card.disabled {
  opacity: 0.6;
  cursor: not-allowed;
  background: rgba(0, 0, 0, 0.2);
}

.status-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 0.75rem;
  padding: 0.4rem 0.8rem;
  border-radius: 20px;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.status-badge.active {
  background: rgba(76, 175, 80, 0.2);
  color: #81c784;
  border: 1px solid rgba(76, 175, 80, 0.3);
}

.status-badge.coming_soon {
  background: rgba(255, 152, 0, 0.2);
  color: #ffb74d;
  border: 1px solid rgba(255, 152, 0, 0.3);
}

.chapter-card h3 {
  font-size: 1.5rem;
  margin: 1.5rem 0 1rem;
  line-height: 1.3;
}

.chapter-card p {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 2rem;
  flex-grow: 1;
}

.action-arrow {
  align-self: flex-end;
  font-size: 1.5rem;
  opacity: 0;
  transform: translateX(-10px);
  transition: all 0.3s ease;
  color: #64b5f6;
}

.chapter-card:hover:not(.disabled) .action-arrow {
  opacity: 1;
  transform: translateX(0);
}
</style>
