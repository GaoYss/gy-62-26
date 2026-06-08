import { api } from './api'

export const appointmentsApi = {
  list: () => api.get('/appointments/'),
  create: (payload) => api.post('/appointments/', payload),
  update: (id, payload) => api.put(`/appointments/${id}/`, payload),
  remove: (id) => api.delete(`/appointments/${id}/`)
}
