<script setup>
defineProps({
  question: Object,
  selectedAnswer: Number,
  showResult: Boolean
})

const emit = defineEmits(['select-answer'])

const handleSelect = (index) => {
  emit('select-answer', index)
}
</script>

<template>
  <div class="quiz-card">
    <div class="header-section">
      <h2 class="question-text">{{ question.question }}</h2>
      
      <!-- Code Snippet Section -->
      <div v-if="question.code" class="code-block">
        <pre><code>{{ question.code }}</code></pre>
      </div>
    </div>
    
    <div class="options-container">
      <button 
        v-for="(option, index) in question.options" 
        :key="index"
        class="option-btn"
        :class="{
          'selected': selectedAnswer === index,
          'correct': showResult && index === question.answer,
          'wrong': showResult && selectedAnswer === index && selectedAnswer !== question.answer,
          'disabled': showResult
        }"
        @click="!showResult && handleSelect(index)"
        :disabled="showResult"
      >
        <span class="option-letter">{{ ['A', 'B', 'C', 'D'][index] }}</span>
        <span class="option-text">{{ option }}</span>
        
        <span v-if="showResult && index === question.answer" class="icon-result">✓</span>
        <span v-if="showResult && selectedAnswer === index && selectedAnswer !== question.answer" class="icon-result">✗</span>
      </button>
    </div>

    <div v-if="showResult" class="explanation">
      <p><strong>Explication :</strong> {{ question.explanation }}</p>
    </div>
  </div>
</template>

<style scoped>
.quiz-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 2rem;
  width: 100%;
  max-width: 700px;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  color: white;
  animation: fadeIn 0.5s ease-out;
}

@media (max-width: 600px) {
  .quiz-card {
    padding: 1.5rem;
  }
}

.question-text {
  font-size: 1.4rem;
  margin-bottom: 1.5rem;
  font-weight: 600;
  text-align: left;
  line-height: 1.4;
  background: linear-gradient(to right, #fff, #b3d5ff);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media (max-width: 600px) {
  .question-text {
    font-size: 1.1rem;
    margin-bottom: 1rem;
  }
  
  .option-btn {
    padding: 0.8rem 1rem;
  }
  
  .option-text {
    font-size: 0.9rem;
  }
}

/* Code Block Styling */
.code-block {
  background: #1e1e1e;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 2rem;
  border: 1px solid #333;
  overflow-x: auto;
  box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);
}

.code-block pre {
  margin: 0;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.95rem;
  color: #d4d4d4;
}

.code-block code {
  white-space: pre-wrap;
}

.options-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.option-btn {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  color: #fff;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
  position: relative;
}

.option-btn:hover:not(.disabled) {
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(5px);
}

.option-btn.selected {
  background: rgba(100, 181, 246, 0.3);
  border-color: rgba(100, 181, 246, 0.5);
}

.option-btn.correct {
  background: rgba(76, 175, 80, 0.3) !important;
  border-color: rgba(76, 175, 80, 0.8) !important;
}

.option-btn.wrong {
  background: rgba(244, 67, 54, 0.3) !important;
  border-color: rgba(244, 67, 54, 0.8) !important;
}

.option-letter {
  background: rgba(255, 255, 255, 0.15);
  min-width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  font-weight: 700;
  font-size: 0.9rem;
  color: #e0e0e0;
}

.option-text {
  flex-grow: 1;
  font-size: 1rem;
}

.icon-result {
  font-weight: bold;
  font-size: 1.2rem;
  margin-left: 10px;
}

.explanation {
  margin-top: 2rem;
  padding: 1.2rem;
  background: rgba(100, 181, 246, 0.1);
  border-radius: 12px;
  border-left: 4px solid #64b5f6;
  font-size: 0.95rem;
  line-height: 1.6;
  animation: slideDown 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
