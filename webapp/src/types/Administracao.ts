export type UserGrid = {
  id: number
  username: string
  email: string
  name: string
  company: string
  profile: string
}

export type ProfileOut = {
  id: number
  name: string
}

export type CompanyOut = {
  id: number
  name: string
}

export type UserIn = {
  id: number
  username: string
  email: string
  name: string
  company: number
  profile: Number
}