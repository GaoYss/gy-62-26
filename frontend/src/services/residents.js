import { api } from './api'

export const residentsApi = {
  list: () => api.get('/residents/'),
  create: (payload) => api.post('/residents/', payload),
  update: (id, payload) => api.put(`/residents/${id}/`, payload),
  remove: (id) => api.delete(`/residents/${id}/`)
}
