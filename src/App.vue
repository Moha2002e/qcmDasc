<script setup>
import { ref, computed } from 'vue'
import questionsData from './data/questions.json'
import chaptersData from './data/chapters.json'
import QuizCard from './components/QuizCard.vue'
import ResultCard from './components/ResultCard.vue'
import ChapterMenu from './components/ChapterMenu.vue'

// --- State Management ---
const currentView = ref('menu') // 'menu' or 'quiz'
const activeChapter = ref(null)

// Quiz State
const questions = ref(questionsData)
const currentQuestionIndex = ref(0)
const score = ref(0)
const isFinished = ref(false)
const userAnswers = ref([])
const selectedAnswer = ref(null)
const showResult = ref(false)

const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
const progress = computed(() => ((currentQuestionIndex.value) / questions.value.length) * 100)

// --- Navigation Methods ---

const startChapter = (chapterId) => {
  const chapter = chaptersData.find(c => c.id === chapterId)
  if (chapter) {
    activeChapter.value = chapter
    currentView.value = 'quiz'
    restartQuiz() // Ensure we start fresh
  }
}

const goHome = () => {
  currentView.value = 'menu'
  activeChapter.value = null
}

// --- Quiz Logic ---

const handleAnswerSelection = (index) => {
  if (showResult.value) return

  selectedAnswer.value = index
  showResult.value = true
  
  const isCorrect = index === currentQuestion.value.answer
  if (isCorrect) score.value++

  userAnswers.value.push({
    questionId: currentQuestion.value.id,
    selectedIndex: index,
    isCorrect: isCorrect
  })

  // Auto-advance
  setTimeout(() => nextQuestion(), 2500)
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

    <!-- View: Chapter Selection Menu -->
    <main v-if="currentView === 'menu'" class="content-wrapper menu-wrapper">
      <ChapterMenu @select-chapter="startChapter" />
    </main>

    <!-- View: Active Quiz -->
    <main v-else class="content-wrapper quiz-wrapper">
      <button class="back-btn" @click="goHome">
        ← Menu
      </button>

      <div v-if="!isFinished" class="quiz-container">
        <div class="header">
          <small class="chapter-label">Chapitre {{ activeChapter.id }}</small>
          <h1>{{ activeChapter.title }}</h1>
          
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
        <button class="menu-btn" @click="goHome">Choisir un autre chapitre</button>
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

.blob-1 { top: -10%; left: -10%; width: 500px; height: 500px; background: #7c4dff; animation: float 20s infinite alternate; }
.blob-2 { bottom: -10%; right: -10%; width: 600px; height: 600px; background: #00bcd4; animation: float 25s infinite alternate-reverse; }
.blob-3 { top: 40%; left: 40%; width: 400px; height: 400px; background: #e91e63; animation: float 22s infinite alternate; }

.content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 2rem;
}

.menu-wrapper {
  justify-content: flex-start;
  padding-top: 5rem;
}

/* Quiz Styles */
.quiz-container {
  width: 100%;
  max-width: 700px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
  animation: fadeIn 0.5s ease-out;
}

.header {
  text-align: center;
  width: 100%;
  margin-bottom: 1rem;
}

.chapter-label {
  text-transform: uppercase;
  letter-spacing: 2px;
  opacity: 0.6;
  font-size: 0.8rem;
  display: block;
  margin-bottom: 0.5rem;
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

/* Buttons */
.back-btn {
  position: absolute;
  top: 2rem;
  left: 2rem;
  background: none;
  border: 1px solid rgba(255,255,255,0.2);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.back-btn:hover {
  background: rgba(255,255,255,0.1);
}

.menu-btn {
  margin-top: 1rem;
  background: transparent;
  border: 1px solid rgba(255,255,255,0.3);
  color: rgba(255,255,255,0.8);
  padding: 1rem 2rem;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.2s;
}

.menu-btn:hover {
  background: rgba(255,255,255,0.1);
  color: white;
  border-color: white;
}

/* Utility */
@keyframes float {
  0% { transform: translate(0, 0); }
  100% { transform: translate(50px, 50px); }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.result-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
