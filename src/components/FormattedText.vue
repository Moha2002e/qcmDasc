<script setup>
import { computed } from 'vue'

const props = defineProps({
  text: {
    type: String,
    required: true
  }
})

const parsedContent = computed(() => {
  if (!props.text) return []
  
  // Regex to capture ```lang ... ``` blocks
  // Group 1: Language (optional)
  // Group 2: Code content
  const codeBlockRegex = /```(\w*)\s*([\s\S]*?)```/g
  
  const result = []
  let lastIndex = 0
  let match
  
  while ((match = codeBlockRegex.exec(props.text)) !== null) {
    // Text before the code block
    if (match.index > lastIndex) {
      result.push({
        type: 'text',
        content: props.text.slice(lastIndex, match.index)
      })
    }
    
    // The code block itself
    result.push({
      type: 'code',
      language: match[1] || 'text',
      content: match[2].trim() // Trim to avoid extra newlines at start/end
    })
    
    lastIndex = codeBlockRegex.lastIndex
  }
  
  // Text after the last code block (or whole text if no code)
  if (lastIndex < props.text.length) {
    result.push({
      type: 'text',
      content: props.text.slice(lastIndex)
    })
  }
  
  return result
})
</script>

<template>
  <div class="formatted-text">
    <template v-for="(part, index) in parsedContent" :key="index">
      
      <!-- Regular Text -->
      <span v-if="part.type === 'text'" class="text-segment" v-html="part.content.replace(/\n/g, '<br>')"></span>
      
      <!-- Code Block -->
      <div v-else class="code-container">
        <div class="code-header" v-if="part.language">
          <span class="dot red"></span>
          <span class="dot yellow"></span>
          <span class="dot green"></span>
          <span class="lang-label">{{ part.language }}</span>
        </div>
        <pre><code :class="part.language">{{ part.content }}</code></pre>
      </div>
      
    </template>
  </div>
</template>

<style scoped>
.formatted-text {
  line-height: 1.6;
  width: 100%;
}

.text-segment {
  /* Allow br to work */
  display: inline; 
}

.code-container {
  margin: 1.5rem 0;
  background: #1e1e2ec4; /* Darker, slightly transparent */
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  text-align: left; /* Ensure code is left aligned even if parent is centered */
}

.code-header {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.red { background-color: #ff5f56; }
.yellow { background-color: #ffbd2e; }
.green { background-color: #27c93f; }

.lang-label {
  margin-left: auto;
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.4);
  text-transform: uppercase;
  font-family: sans-serif;
  letter-spacing: 1px;
}

pre {
  margin: 0;
  padding: 1rem;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.2) transparent;
}

pre::-webkit-scrollbar {
  height: 6px;
}
pre::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
}

code {
  font-family: 'Consolas', 'Monaco', 'Andale Mono', 'Ubuntu Mono', monospace;
  font-size: 0.9rem;
  color: #a5f3fc; /* Cyan-ish for visibility */
  line-height: 1.5;
  white-space: pre;
}

/* Rudimentary syntax coloring base */
code.java, code.js, code.javascript {
  color: #e2e8f0;
}
</style>
