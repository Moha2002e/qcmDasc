<script setup>
import { computed } from 'vue'
import { jsPDF } from 'jspdf'

const props = defineProps({
  score: Number,
  totalQuestions: Number,
  userAnswers: Array,
  questions: Array
})

const emit = defineEmits(['restart'])

const wrongAnswers = computed(() => {
  if (!props.questions || !props.userAnswers) return []
  
  // Map user answers to questions to find the wrong ones
  return props.userAnswers
    .map((ans, index) => {
      // Find the corresponding question. 
      // Assuming userAnswers are pushed in the same order as questions since we just go 1..N
      // But safer to lookup by ID if feasible. 
      // App.vue pushes { questionId, ... } so let's use that.
      const question = props.questions.find(q => q.id === ans.questionId)
      if (!question) return null
      
      return {
        question,
        userSelected: ans.selectedIndex,
        isCorrect: ans.isCorrect
      }
    })
    .filter(item => item && !item.isCorrect)
})

const downloadPDF = () => {
  const doc = new jsPDF()
  
  // Title
  doc.setFontSize(22)
  doc.setTextColor(44, 62, 80)
  doc.text("Rapport d'erreurs - QCM", 105, 20, { align: 'center' })
  
  doc.setFontSize(12)
  doc.setTextColor(100)
  doc.text(`Score: ${props.score} / ${props.totalQuestions}`, 105, 30, { align: 'center' })

  let y = 50
  const margin = 20
  const pageWidth = 210
  const maxWidth = pageWidth - (margin * 2)

  if (wrongAnswers.value.length === 0) {
    doc.setFontSize(14)
    doc.setTextColor(40, 167, 69) // Green
    doc.text("Félicitations ! Aucune erreur à signaler 👏", 105, 60, { align: 'center' })
  } else {
    wrongAnswers.value.forEach((item, index) => {
      // Check for page break
      if (y > 250) {
        doc.addPage()
        y = 20
      }

      // Question
      doc.setFontSize(12)
      doc.setTextColor(0, 0, 0)
      doc.setFont("helvetica", "bold")
      
      const questionTitle = `Question ${index + 1}: ${item.question.question}`
      const splitTitle = doc.splitTextToSize(questionTitle, maxWidth)
      doc.text(splitTitle, margin, y)
      y += splitTitle.length * 7

      // User Answer (Wrong)
      doc.setFont("helvetica", "normal")
      doc.setFontSize(11)
      doc.setTextColor(220, 53, 69) // Red
      const wrongTxt = `❎ Votre réponse : ${item.question.options[item.userSelected]}`
      const splitWrong = doc.splitTextToSize(wrongTxt, maxWidth)
      doc.text(splitWrong, margin + 5, y)
      y += splitWrong.length * 6

      // Correct Answer
      doc.setTextColor(40, 167, 69) // Green
      const correctTxt = `✅ Bonne réponse : ${item.question.options[item.question.answer]}`
      const splitCorrect = doc.splitTextToSize(correctTxt, maxWidth)
      doc.text(splitCorrect, margin + 5, y)
      y += splitCorrect.length * 6

      // Explanation
      if (item.question.explanation) {
        doc.setTextColor(80, 80, 80) // Gray
        doc.setFont("helvetica", "italic")
        const explTxt = `Explication : ${item.question.explanation}`
        const splitExpl = doc.splitTextToSize(explTxt, maxWidth)
        doc.text(splitExpl, margin + 5, y)
        y += splitExpl.length * 6
      }

      y += 10 // Spacing
    })
  }

  doc.save("resultat_qcm.pdf")
}

</script>

<template>
  <div class="result-card-container">
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

      <button class="pdf-btn" @click="downloadPDF">
        📥 Télécharger le résultat (PDF)
      </button>
    </div>

    <!-- Review Section -->
    <div v-if="wrongAnswers.length > 0" class="review-section">
      <h3>Questions à revoir ({{ wrongAnswers.length }})</h3>

      <div v-for="(item, index) in wrongAnswers" :key="index" class="review-item">
        <div class="review-question">
          <strong>Question :</strong> {{ item.question.question }}
        </div>
        
        <div class="review-options">
          <div class="option wrong">
            <span class="icon">❌</span>
            <span class="label">Votre réponse :</span>
            {{ item.question.options[item.userSelected] }}
          </div>
          <div class="option correct">
            <span class="icon">✅</span>
            <span class="label">Bonne réponse :</span>
            {{ item.question.options[item.question.answer] }}
          </div>
        </div>

        <div class="review-explanation" v-if="item.question.explanation">
          <strong>💡 Explication :</strong>
          <p>{{ item.question.explanation }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.result-card-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
  max-width: 800px;
  align-items: center;
}

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
  width: 100%;
  max-width: 500px; /* Keep score card compact */
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

.pdf-btn {
  background: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  color: #333;
  font-weight: 600;
  cursor: pointer;
  display: block;
  margin-top: 1.5rem; 
  transition: all 0.2s;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.pdf-btn:hover {
  background: #f8f9fa;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}

/* Review Section Styles */
.review-section {
  width: 100%;
  animation: fadeIn 1s ease-out;
}

.review-section h3 {
  text-align: center;
  font-size: 1.8rem;
  margin-bottom: 2rem;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 1rem;
  display: inline-block;
  width: 100%;
}

.review-item {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  backdrop-filter: blur(5px);
  transition: transform 0.2s;
}

.review-item:hover {
  background: rgba(255, 255, 255, 0.08);
  transform: scale(1.01);
}

.review-question {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  color: #fff;
}

.review-options {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  margin-bottom: 1rem;
}

.option {
  padding: 0.8rem 1rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-size: 1rem;
}

.option.wrong {
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #fca5a5;
}

.option.correct {
  background: rgba(34, 197, 94, 0.2);
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #86efac;
}

.label {
  font-weight: bold;
  font-size: 0.9em;
  opacity: 0.8;
  min-width: 120px;
}

.review-explanation {
  background: rgba(59, 130, 246, 0.1);
  border-left: 4px solid #3b82f6;
  padding: 1rem;
  border-radius: 0 8px 8px 0;
  margin-top: 1rem;
}

.review-explanation strong {
  display: block;
  margin-bottom: 0.5rem;
  color: #93c5fd;
}

.review-explanation p {
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.5;
  margin: 0;
  font-size: 0.95rem;
}

@media (max-width: 600px) {
  .review-item {
    padding: 1rem;
  }
  .option {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.4rem;
  }
  .label {
    min-width: auto;
  }
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
</style>
