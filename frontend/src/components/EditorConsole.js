import { Box, Grid, TextField } from '@mui/material'

export default function EditorConsole({ input, setInput, outputs }) {
  let output = ''
  for (let i = 0; i < outputs.length; i++) {
    output += outputs[i] + '\n'
  }

  return (
    <Box
      sx={{
        flexGrow: 1,
        marginBottom: 4,
        marginLeft: { md: 4 },
        marginRight: { md: 4 },
      }}
    >
      <Grid container spacing={2}>
        <Grid item xs={12} md={8}>
          <TextField
            fullWidth
            id='filled-multiline-flexible'
            multiline
            rows={20}
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
        </Grid>
        <Grid item xs={12} md={4}>
          <TextField
            fullWidth
            InputProps={{
              readOnly: true,
              disableUnderline: true,
              outline: 'none',
              style: { backgroundColor: 'black', color: 'white' },
            }}
            id='filled-multiline-flexible'
            multiline
            rows={20}
            value={output}
          />
        </Grid>
      </Grid>
    </Box>
  )
}
