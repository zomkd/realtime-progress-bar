<script setup lang="ts">
import { computed, reactive, ref } from 'vue';
import ProgressBar from './components/ProgressBar.vue';
import RpButton from './components/RpButton.vue';

interface ITaskResult {
  done: number,
  total: number, 
}

interface ITaskStatus {
  taskResult: ITaskResult | null;
}

const taskStatus = reactive<ITaskStatus>({
  taskResult: null
});

const isClicked = ref<boolean>(false);
const text = computed(() => isClicked.value ? 'Stop' : 'Start')

const BASE_URL = 'http://127.0.0.1:8000';
const BASE_URL_WS = 'ws://127.0.0.1:8000';

const runTask = () => {
  isClicked.value = !isClicked.value;

  fetch(BASE_URL + '/task', {
    method: 'GET',
  })
  .then(res => res.json())
  .then((res) => {
    const socket = new WebSocket(
      BASE_URL_WS + `/task/${res.task_id}`
        );
        socket.onmessage = (event) => {
          const parsedEvent = JSON.parse(event.data);
          taskStatus.taskResult = parsedEvent.task_result
        };

        socket.onerror = (err) => {
          console.log(err);
        };
        socket.onclose = (event) => {
          console.log(event);
        };
        socket.onopen = (event) => {
          console.log(event);
        };
  }).catch(err => console.log(err))
}
</script>

<template>
  <div class="container" >
    <div class="task-box">
      <div class="task-result">
        <div v-if="taskStatus.taskResult">
          {{ taskStatus.taskResult }}
        </div>
        <div v-else>
          Run task!
        </div>
      </div>
      <progress-bar :data="taskStatus.taskResult" />
      <div class="rp-button">
      <rp-button type="submit" @clicked="runTask" :text="text" :class="isClicked ? 'stop-btn' : 'default-btn'"/>
      </div>
    </div>
</div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
} 
.task-box {
  width: 31.25rem
}

.rp-button {
  margin-top: 5%;
}
</style>
