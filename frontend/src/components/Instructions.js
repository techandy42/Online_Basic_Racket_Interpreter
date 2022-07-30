import { useState } from 'react'
import { Box, Button } from '@mui/material'
import InstructionsContent from './InstructionsContent'

export default function Instructions() {
  const [show, setShow] = useState(false)

  return (
    <Box
      sx={{
        flexGrow: 1,
        marginBottom: 4,
        marginLeft: { md: 4 },
        marginRight: { md: 4 },
      }}
    >
      <Button
        sx={{ marginBottom: 2 }}
        color='inherit'
        variant='contained'
        label='show'
        onClick={() => setShow(!show)}
      >
        {show ? 'Hide Info' : 'Show Info'}
      </Button>
      {show ? <InstructionsContent /> : null}
    </Box>
  )
}
