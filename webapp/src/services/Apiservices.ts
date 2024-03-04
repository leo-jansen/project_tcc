import type { UserIn } from '@/types/Administracao'
import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_ENDPOINT  || 'http://localhost:8081'
})

const ApiService = {
  login: async (username: string, password: string) => {
    const response = await api.post('/auth/singin', {
      username: username,
      password: password
    })
    return response.data
  },
  getUser: async () => {
    const response = await api.get('/auth/token', {
      headers: {
        Authorization: 'bearer ' + localStorage.getItem('system_tcc')
      }
    })
    return response.data
  },
  getAllUser: async () => {
    const response = await api.get('/user/all', {
      headers: {
        Authorization: 'bearer ' + localStorage.getItem('system_tcc')
      }
    })
    return response.data
  },
  getProfile: async () => {
    const response = await api.get('/user/profile', {
      headers: {
        Authorization: 'bearer ' + localStorage.getItem('system_tcc')
      }
    })
    return response.data
  },
  getCompany: async () => {
    const response = await api.get('/user/company', {
      headers: {
        Authorization: 'bearer ' + localStorage.getItem('system_tcc')
      }
    })
    return response.data
  },
  addUser: async (data: UserIn) => {
    const response = await api.post('/auth/singup', data, {
      headers: {
        Authorization: 'bearer ' + localStorage.getItem('system_tcc')
      }
    })
    return response.data
  },
  updateUser: async(id: number, data: UserIn) => {
    const response = await api.put(`/user/${id}`, data, {
      headers: {
        Authorization: 'bearer ' + localStorage.getItem('system_tcc')
      }
    })
    return response.data
  }
}

export default ApiService
