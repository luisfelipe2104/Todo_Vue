<script setup>
import { ref, computed, onMounted, watch } from "vue";
// npm create vite@latest
// npm run dev

const todos = ref([]);
const name = ref("");

const input_content = ref("");
const input_category = ref("");

const todos_asc = computed(() =>
  todos.value.sort((a, b) => {
    return b.created_at - a.created_at;
  })
);
watch(name, (newVal) => {
  localStorage.setItem('name', newVal)
})

onMounted(async () => {
  todos.value = await JSON.parse(localStorage.getItem('todos')) || []
  console.log(typeof todos.value)
  console.log(todos.value)
  name.value = localStorage.getItem('name') || ''
})

const addTodo = () => {
  if (input_content.value.trim() === '' || input_category.value === null) {
    return 
  }
  todos.value.push({
    content: input_content.value,
    category: input_category.value,
    done: false,
    created_at: new Date().getTime()
  })

  input_content.value = ''
}

watch(todos, (newVal) => {
  localStorage.setItem('todos', JSON.stringify(newVal))
}, { deep: true })

const removeTodo = (index) => {
  todos.value.splice(index, 1)
}

</script>

<template>
  <main class="app">
    <section class="greeting">
      <h2 class="title">What's up 
        <input type="text" placeholder="Name here" v-model="name" />
      </h2>
    </section>

    <section class="create-todo">
      <h3>CREATE A TODO</h3>

      <form @submit.prevent="addTodo">
        <h4>What's on your todo?</h4>
        <input type="text" placeholder="e.g. drink water" 
          v-model="input_content">

        <h4>Pick a category</h4>
        <div class="options">
          <label>
            <input 
              checked
              type="radio" 
              name='category'
              value="business"
              v-model="input_category"
              >
              <span class="bubble business"></span>
              <div>Not Urgent</div>
            </label>

            <label>
              <input 
                type="radio" 
                name='category'
                value="personal"
                v-model="input_category"
                >
                <span class="bubble personal"></span>
              <div>Urgent</div>
            </label>
        </div>
        <input type="submit" value="Add Todo">
      </form>
    </section>

    <section class="todo-list">
      <h3>TODO LIST</h3>
      <div class="list">
        <div v-for="todo, index in todos_asc" :class="`todo-item ${todo.done && 'done'}`">
          <label>
            <input type="checkbox" v-model="todo.done">
            <span :class="`bubble ${todo.category}`"></span>
          </label>

          <div class="todo-content">
            <input type="text" v-model="todo.content">
          </div>

          <div class="actions">
            <button class="delete" @click="removeTodo(index)">Delete</button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
