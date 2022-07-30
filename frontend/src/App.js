import { useState } from 'react'
import NavBar from './components/NavBar'
import EditorConsole from './components/EditorConsole'
import Box from '@mui/material/Box'

export default function App() {
  const [input, setInput] = useState('')
  const [outputs, setOutputs] = useState([])
  const [result, setResult] = useState(false)

  return (
    <Box>
      <NavBar input={input} setOutputs={setOutputs} setResult={setResult} />
      <EditorConsole input={input} setInput={setInput} outputs={outputs} />
    </Box>
  )
}
