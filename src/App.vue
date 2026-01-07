<script setup>
import { ref, computed } from 'vue'
import questionsChap1 from './data/questions_chap1.json'
import questionsChap2 from './data/questions_chap2.json'
import questionsChap3 from './data/questions_chap3.json'
import questionsChap4 from './data/questions_chap4.json'
import questionsChap5 from './data/questions_chap5.json'
import questionsChap6 from './data/questions_chap6.json'
import questionsChap7 from './data/questions_chap7.json'
import questionsChap9 from './data/questions_chap9.json'
import questionsChap10 from './data/questions_chap10.json'
import chaptersData from './data/chapters.json'
import QuizCard from './components/QuizCard.vue'
import ResultCard from './components/ResultCard.vue'
import ChapterMenu from './components/ChapterMenu.vue'

// Combine for cases needing all questions (like exams)
const allQuestions = [
  ...questionsChap1, 
  ...questionsChap2, 
  ...questionsChap3, 
  ...questionsChap4,
  ...questionsChap5,
  ...questionsChap6,
  ...questionsChap7
]

const questionsMap = {
  1: questionsChap1,
  2: questionsChap2,
  3: questionsChap3,
  4: questionsChap4,
  5: questionsChap5,
  6: questionsChap6,
  7: questionsChap7,
  9: questionsChap9,
  10: questionsChap10
}

// --- State Management ---
const currentView = ref('menu') // 'menu' or 'quiz'
const activeChapter = ref(null)

// Quiz State
// We start with empty, it will be populated by initQuiz
const questions = ref([])
const currentQuestionIndex = ref(0)
const score = ref(0)
const isFinished = ref(false)
const userAnswers = ref([])
const selectedAnswer = ref(null)
const showResult = ref(false)

const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
const progress = computed(() => {
  if (questions.value.length === 0) return 0
  return ((currentQuestionIndex.value) / questions.value.length) * 100
})

// --- Utilities ---
const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

const initQuiz = () => {
  // Determine source questions
  let validQuestions = []
  
  if (activeChapter.value) {
    // Specific chapter
    if (questionsMap[activeChapter.value.id]) {
      validQuestions = questionsMap[activeChapter.value.id]
    } else if (activeChapter.value.id === 8) {
      // Examen Final: 50 questions réparties équitablement (7/8 par chapitre)
      validQuestions = []
      const chapters = [1, 2, 3, 4, 5, 6, 7]
      
      chapters.forEach((chapId, index) => {
        if (questionsMap[chapId]) {
          // Copie et mélange des questions du chapitre
          const pool = shuffleArray([...questionsMap[chapId]])
          // 50 / 7 = 7 reste 1. Le premier chapitre donne 8 questions, les autres 7.
          const count = 7 + ((index === 0) ? 1 : 0)
          validQuestions.push(...pool.slice(0, count))
        }
      })
    } else if (activeChapter.value.id === 9) {
      // Examen difficile : Questions pièges exclusives du fichier chap9
      validQuestions = questionsChap9
    }
  } else {
    validQuestions = allQuestions
  }

  // Deep clone and shuffle questions
  const rawQuestions = JSON.parse(JSON.stringify(validQuestions))
  
  const shuffled = shuffleArray(rawQuestions).map(q => {
    // Determine original correct answer text
    const correctAnswerText = q.options[q.answer]
    
    // Shuffle options
    const shuffledOptions = shuffleArray([...q.options])
    
    // Find new index of the correct answer
    const newAnswerIndex = shuffledOptions.indexOf(correctAnswerText)
    
    return {
      ...q,
      options: shuffledOptions,
      answer: newAnswerIndex
    }
  })
  
  questions.value = shuffled
  
  // Reset state
  currentQuestionIndex.value = 0
  score.value = 0
  isFinished.value = false
  userAnswers.value = []
  selectedAnswer.value = null
  showResult.value = false
}

// --- Navigation Methods ---

const startChapter = (chapterId) => {
  const chapter = chaptersData.find(c => c.id === chapterId)
  if (chapter) {
    activeChapter.value = chapter
    currentView.value = 'quiz'
    initQuiz()
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

  // Auto-advance removed to allow reading explanation
  // setTimeout(() => nextQuestion(), 2500)
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
  initQuiz()
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

        <button v-if="showResult" class="next-btn" @click="nextQuestion">
          Question Suivante →
        </button>
      </div>

      <div v-else class="result-container">
        <ResultCard 
          :score="score"
          :totalQuestions="questions.length"
          :userAnswers="userAnswers"
          :questions="questions"
          @restart="restartQuiz"
        />
        <button class="menu-btn" @click="goHome">Choisir un autre chapitre</button>
      </div>
    </main>
    
    <!-- Explicit spacer for mobile scrolling -->
    <div class="mobile-spacer"></div>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  /* Fallback for browsers ensuring 100vh */
  min-height: 100dvh; 
  width: 100%;
  position: relative;
  overflow-x: hidden;
  background-color: #0f172a;
  font-family: 'Inter', sans-serif;
  color: white;
  /* Ensure space at bottom for mobile scrolling */
  padding-bottom: 15rem; 
}

.content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 2rem;
}

.menu-wrapper {
  justify-content: flex-start;
  padding-top: 5rem;
}

@media (max-width: 600px) {
  .content-wrapper {
    padding: 1rem;
  }
  .menu-wrapper {
    padding-top: 2rem;
  }
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

@media (max-width: 600px) {
  h1 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
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

@media (max-width: 600px) {
  .back-btn {
    top: 1rem;
    left: 1rem;
    padding: 0.4rem 0.8rem;
    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(4px);
    z-index: 100;
  }
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

.next-btn {
  background: #3a7bd5;
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.2);
  margin-top: 1rem;
  animation: fadeIn 0.3s ease-out;
}

.next-btn:hover {
  background: #00d2ff;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.3);
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

.mobile-spacer {
  height: 0;
}

@media (max-width: 600px) {
  .mobile-spacer {
    height: 15vh;
    display: block;
  }
}
</style>
