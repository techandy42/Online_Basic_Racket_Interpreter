import { useState } from 'react'
import NavBar from './components/NavBar'
import EditorConsole from './components/EditorConsole'
import Instructions from './components/Instructions'
import { Box, Divider } from '@mui/material'

export default function App() {
  const [input, setInput] = useState('')
  const [outputs, setOutputs] = useState([])
  const [result, setResult] = useState(false)

  return (
    <Box>
      <NavBar input={input} setOutputs={setOutputs} setResult={setResult} />
      <EditorConsole input={input} setInput={setInput} outputs={outputs} />
      <Divider sx={{ marginBottom: 2 }} />
      <Instructions />
    </Box>
  )
}
