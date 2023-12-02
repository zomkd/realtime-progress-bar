<script setup lang="ts">
import { computed, reactive, ref } from 'vue';
import ProgressBar from './components/ProgressBar.vue';
import RpButton from './components/RpButton.vue';

interface ITaskResult {
  done: number,
  total: number, 
}

type TaskStatus = string

interface ITask {
  taskResult: ITaskResult | null;
  taskStatus: TaskStatus | null;
}

const task = reactive<ITask>({
  taskResult: null,
  taskStatus: null

});

const BASE_URL = 'http://127.0.0.1:8000';
const BASE_URL_WS = 'ws://127.0.0.1:8000';

const socket = computed(() => {
  if (taskID.value) {
    return new WebSocket(
      BASE_URL_WS + `/task/${taskID.value}`
        );
  }
  return null;
});

const btnText = 'START';
const taskID = ref<string>('');

const info = computed(() => task.taskStatus === 'SUCCESS' || task.taskStatus === null ? 'Run task!' : task.taskResult)
const isClicked = computed(() => task.taskStatus === 'SUCCESS' || task.taskStatus === null ? false : true)

const runTask = async () => {

  await fetch(BASE_URL + '/task', {
    method: 'GET',
  })
  .then(res => res.json())
  .then((res) => {
    taskID.value = res.task_id;
    socket.value!.onmessage = (event) => {
      const parsedEvent = JSON.parse(event.data);
      task.taskStatus = parsedEvent.task_status
      task.taskResult = parsedEvent.task_result
    };
    socket.value!.onerror = (err) => {
      console.log(err);
    };
    socket.value!.onclose = (event) => {
      console.log(event);
    };
    socket.value!.onopen = (event) => {
      console.log(event);
    };
  }).catch(err => console.log(err))
}

</script>

<template>
  <div class="container" >
    <div class="task-box">
      <div class="task-result">
        <div> {{ info }}</div>
      </div>
      <progress-bar :data="task.taskResult" />
      <div class="rp-button">
        <rp-button type="submit" @clicked="runTask" :text="btnText" :disabled="isClicked"/>
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
