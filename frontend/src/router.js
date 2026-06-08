import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from './views/DashboardView.vue'
import ResidentsView from './views/ResidentsView.vue'
import AppointmentsView from './views/AppointmentsView.vue'
import VisitRecordsView from './views/VisitRecordsView.vue'
import NotificationsView from './views/NotificationsView.vue'

const routes = [
  { path: '/', name: 'dashboard', component: DashboardView },
  { path: '/residents', name: 'residents', component: ResidentsView },
  { path: '/appointments', name: 'appointments', component: AppointmentsView },
  { path: '/visits', name: 'visits', component: VisitRecordsView },
  { path: '/notifications', name: 'notifications', component: NotificationsView }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
