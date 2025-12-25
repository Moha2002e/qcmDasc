<script setup>
defineProps({
  score: Number,
  totalQuestions: Number,
  userAnswers: Array
})

const emit = defineEmits(['restart'])
</script>

<template>
  <div class="result-card">
    <div class="score-circle">
      <span class="score-number">{{ score }}</span>
      <span class="score-total">/ {{ totalQuestions }}</span>
    </div>
    
    <h2 class="result-title">
      <span v-if="score === totalQuestions">Parfait ! 🏆</span>
      <span v-else-if="score >= totalQuestions / 2">Bien joué ! 👍</span>
      <span v-else>Peut mieux faire... 💪</span>
    </h2>

    <button class="restart-btn" @click="$emit('restart')">
      Recommencer le Quiz
    </button>
  </div>
</template>

<style scoped>
.result-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 3rem;
  text-align: center;
  color: white;
  animation: fadeIn 0.8s ease-out;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  display: flex;
  flex-direction: column;
  align-items: center;
}

@media (max-width: 600px) {
  .result-card {
    padding: 2rem;
  }
  .score-circle {
    width: 120px;
    height: 120px;
  }
  .score-number {
    font-size: 2.5rem;
  }
  .result-title {
    font-size: 1.5rem;
  }
}

.score-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 8px solid rgba(255, 255, 255, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 auto 2rem;
  position: relative;
  background: rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 20px rgba(0,0,0,0.5);
}

.score-number {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1;
  background: linear-gradient(135deg, #FFD700, #FFA500);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.score-total {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.7);
  margin-top: 5px;
}

.result-title {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.restart-btn {
  background: linear-gradient(45deg, #2196F3, #21CBF3);
  border: none;
  padding: 1rem 2.5rem;
  border-radius: 50px;
  color: white;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 15px rgba(33, 203, 243, 0.4);
}

.restart-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(33, 203, 243, 0.6);
}

.restart-btn:active {
  transform: translateY(1px);
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
</style>
