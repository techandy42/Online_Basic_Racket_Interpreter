import { useState } from 'react'
import { AppBar, Box, Toolbar, Typography, Button } from '@mui/material'
import axios from 'axios'

export default function NavBar({ input, setOutputs, setResult }) {
  const [running, setRunning] = useState(false)
  const [step, setStep] = useState(false)

  const handleClear = () => {
    if (running) return

    setOutputs([])
    setResult(false)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (running) return

    setRunning(true)

    console.log(step)
    console.log('submitted...')

    const result = await axios.post(
      'https://racket-interpreter.herokuapp.com/',
      {
        input: input,
        show_steps: step,
      },
    )
    setOutputs(result.data.outputs)
    setResult(result.data.result)

    setRunning(false)
    setStep(false)
  }

  return (
    <Box sx={{ flexGrow: 1, marginBottom: 4 }}>
      <form onSubmit={handleSubmit}>
        <AppBar position='static' color='transparent'>
          <Toolbar>
            <Typography variant='h6' component='div' sx={{ flexGrow: 1 }}>
              (λ) Racket Interpreter
            </Typography>
            <Button
              sx={{ marginLeft: { xs: 1, md: 2 } }}
              color='success'
              variant={running ? 'outlined' : 'contained'}
              type='submit'
              label='run'
            >
              Run
            </Button>
            <Button
              sx={{ marginLeft: { xs: 1, md: 2 } }}
              variant={running ? 'outlined' : 'contained'}
              type='submit'
              label='step'
              onClick={() => {
                setStep(true)
              }}
            >
              Step
            </Button>
            <Button
              sx={{ marginLeft: { xs: 1, md: 2 } }}
              color='inherit'
              variant={running ? 'outlined' : 'contained'}
              label='clear'
              onClick={() => handleClear()}
            >
              Clear
            </Button>
          </Toolbar>
        </AppBar>
      </form>
    </Box>
  )
}
