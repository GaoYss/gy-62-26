<template>
  <section>
    <PageHeader eyebrow="通知" title="紧急通知" description="发布面向家属、员工或全体人员的重要信息。" />

    <article class="panel">
      <h3>发布通知</h3>
      <NotificationForm :model="form" @submit="saveNotification" />
      <p v-if="message" class="message">{{ message }}</p>
    </article>

    <article class="panel">
      <h3>通知列表</h3>
      <EmptyState v-if="notifications.length === 0" />
      <div v-else class="notice-grid">
        <div v-for="item in notifications" :key="item.id" class="notice-card">
          <div class="notice-title">
            <strong>{{ item.title }}</strong>
            <span :class="['badge', item.level]">{{ levelText[item.level] }}</span>
          </div>
          <p>{{ item.content }}</p>
          <footer>
            <span>{{ targetText[item.target_group] }}</span>
            <span>{{ item.is_active ? '有效' : '已停用' }}</span>
            <span>{{ formatTime(item.published_at) }}</span>
          </footer>
        </div>
      </div>
    </article>
  </section>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import EmptyState from '../components/EmptyState.vue'
import NotificationForm from '../components/NotificationForm.vue'
import PageHeader from '../components/PageHeader.vue'
import { notificationsApi } from '../services/notifications'

const notifications = ref([])
const message = ref('')
const levelText = { info: '普通', warning: '重要', critical: '紧急' }
const targetText = { all: '全部', families: '家属', staff: '员工' }
const initialForm = {
  title: '',
  content: '',
  level: 'warning',
  target_group: 'families',
  is_active: true
}
const form = reactive({ ...initialForm })

onMounted(loadNotifications)

async function loadNotifications() {
  notifications.value = (await notificationsApi.list()).results
}

async function saveNotification() {
  await notificationsApi.create(form)
  Object.assign(form, initialForm)
  message.value = '通知已发布'
  await loadNotifications()
}

function formatTime(value) {
  return value ? new Date(value).toLocaleString('zh-CN') : ''
}
</script>
