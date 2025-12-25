<script setup>
import { ref, computed } from 'vue'
import questionsData from './data/questions.json'
import QuizCard from './components/QuizCard.vue'
import ResultCard from './components/ResultCard.vue'

const questions = ref(questionsData)
const currentQuestionIndex = ref(0)
const score = ref(0)
const isFinished = ref(false)
const userAnswers = ref([]) // Stores { questionId, selectedIndex, isCorrect }
const selectedAnswer = ref(null)
const showResult = ref(false) // Show immediate result after selection

const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
const progress = computed(() => ((currentQuestionIndex.value) / questions.value.length) * 100)

const handleAnswerSelection = (index) => {
  if (showResult.value) return // Prevent changing answer after selection

  selectedAnswer.value = index
  showResult.value = true
  
  const isCorrect = index === currentQuestion.value.answer
  if (isCorrect) {
    score.value++
  }

  userAnswers.value.push({
    questionId: currentQuestion.value.id,
    selectedIndex: index,
    isCorrect: isCorrect
  })

  // Auto-advance after small delay
  // Optional: Remove timeout if you want manual "Next" button
  setTimeout(() => {
    nextQuestion()
  }, 2500)
}

const nextQuestion = () => {
  if (currentQuestionIndex.value < questions.value.length - 1) {
    currentQuestionIndex.value++
    selectedAnswer.value = null
    showResult.value = false
  } else {
    isFinished.value = true
  }
}

const restartQuiz = () => {
  currentQuestionIndex.value = 0
  score.value = 0
  isFinished.value = false
  userAnswers.value = []
  selectedAnswer.value = null
  showResult.value = false
}
</script>

<template>
  <div class="app-container">
    <div class="background-blobs">
      <div class="blob blob-1"></div>
      <div class="blob blob-2"></div>
      <div class="blob blob-3"></div>
    </div>

    <main class="content-wrapper">
      <div v-if="!isFinished" class="quiz-container">
        <div class="header">
          <h1>Communication Réseaux en C</h1>
          <div class="progress-bar-container">
            <div class="progress-bar" :style="{ width: progress + '%' }"></div>
          </div>
          <p class="question-counter">Question {{ currentQuestionIndex + 1 }} / {{ questions.length }}</p>
        </div>

        <QuizCard 
          :question="currentQuestion"
          :selectedAnswer="selectedAnswer"
          :showResult="showResult"
          @select-answer="handleAnswerSelection"
        />
      </div>

      <div v-else class="result-container">
        <ResultCard 
          :score="score"
          :totalQuestions="questions.length"
          :userAnswers="userAnswers"
          @restart="restartQuiz"
        />
      </div>
    </main>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  width: 100%;
  position: relative;
  overflow-x: hidden;
  background-color: #0f172a;
  font-family: 'Inter', sans-serif;
  color: white;
}

.background-blobs {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  pointer-events: none;
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.6;
}

.blob-1 {
  top: -10%;
  left: -10%;
  width: 500px;
  height: 500px;
  background: #7c4dff;
  animation: float 20s infinite alternate;
}

.blob-2 {
  bottom: -10%;
  right: -10%;
  width: 600px;
  height: 600px;
  background: #00bcd4;
  animation: float 25s infinite alternate-reverse;
}

.blob-3 {
  top: 40%;
  left: 40%;
  width: 400px;
  height: 400px;
  background: #e91e63;
  animation: float 22s infinite alternate;
}

.content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 2rem;
}

.quiz-container {
  width: 100%;
  max-width: 700px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.header {
  text-align: center;
  width: 100%;
  margin-bottom: 1rem;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.progress-bar-container {
  width: 100%;
  height: 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #00d2ff, #3a7bd5);
  transition: width 0.5s ease-out;
}

.question-counter {
  font-size: 0.9rem;
  opacity: 0.7;
}

@keyframes float {
  0% { transform: translate(0, 0); }
  100% { transform: translate(50px, 50px); }
}
</style>
