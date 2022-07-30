import { Box, Card, Typography, CardContent } from '@mui/material'

export default function InstructionsContent() {
  const builtinFunctions =
    'cond, else, true, false, =, >, <, >= , <=, add1, sub1, +, -, *, /, %, expt, sqr, sqrt, floor, ceiling, round, abs, max, min, gcd, lcm, sin, cos, tan, log, printf'
  const builtinConstants = 'pi, e'

  return (
    <Box fullWidth>
      <Card sx={{ marginBottom: 2 }}>
        <CardContent>
          <Typography variant='h6'>Features</Typography>
          <ul>
            <li>
              <Typography>numeric and boolean types supported</Typography>
            </li>
            <li>
              <Typography>basic operations</Typography>
            </li>
            <Typography>(+ 2 3)</Typography>
            <li>
              <Typography>builtin functions</Typography>
            </li>
            <Typography>(gcd 12 18)</Typography>
            <li>
              <Typography>builtin constants</Typography>
            </li>
            <Typography>pi</Typography>
            <li>
              <Typography>console output</Typography>
            </li>
            <Typography>(printf 5)</Typography>
            <li>
              <Typography>custom functions</Typography>
            </li>
            <Typography>(define (add_two a b) (+ a b))</Typography>
            <li>
              <Typography>custom constants</Typography>
            </li>
            <Typography>(define x 10)</Typography>
          </ul>
        </CardContent>
      </Card>
      <Card sx={{ marginBottom: 2 }}>
        <CardContent>
          <Typography variant='h6'>Builtin Functions and Constants</Typography>
          <ul>
            <li>
              <Typography>{builtinFunctions}</Typography>
            </li>
            <li>
              <Typography>{builtinConstants}</Typography>
            </li>
          </ul>
        </CardContent>
      </Card>
      <Card sx={{ marginBottom: 2 }}>
        <CardContent>
          <Typography variant='h6'>Specfication</Typography>
          <ul>
            <li>
              <Typography>
                Only numeric and boolean types are supported.
              </Typography>
            </li>
            <li>
              <Typography>
                Console output must be made by using the <strong>printf</strong>{' '}
                function.
              </Typography>
            </li>
            <li>
              <Typography>
                The cond conditionals can be written with both{' '}
                <strong>()</strong> and <strong>[]</strong> notation.
              </Typography>
            </li>
            <li>
              <Typography>
                There cannot be any duplicate definition names or parameter
                names that are already defined as definition names.
              </Typography>
            </li>
            <li>
              <Typography>
                There can be numeric or boolean values in a cond without an
                operation block <strong>()</strong>.
              </Typography>
            </li>
          </ul>
        </CardContent>
      </Card>
      <Card sx={{ marginBottom: 2 }}>
        <CardContent>
          <Typography variant='h6'>Sample #1 - Add Two</Typography>
          <ul>
            <Typography>(define x 10)</Typography>
            <Typography>(define y (* 2 3))</Typography>
            <br />
            <Typography>(define (add-two a b)</Typography>
            <Typography>&nbsp;&nbsp;&nbsp;&nbsp;(+ a b))</Typography>
            <br />
            <Typography>(printf (add-two x y))</Typography>
          </ul>
        </CardContent>
      </Card>
      <Card sx={{ marginBottom: 2 }}>
        <CardContent>
          <Typography variant='h6'>Sample #2 - Factorial</Typography>
          <ul>
            <Typography>(define (factorial n)</Typography>
            <Typography>&nbsp;&nbsp;&nbsp;&nbsp;(cond [(= n 1) 1]</Typography>
            <Typography>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[else (* n
              (factorial (sub1 n)))]))
            </Typography>
            <br />
            <Typography>(printf (factorial 10))</Typography>
          </ul>
        </CardContent>
      </Card>
      <Card sx={{ marginBottom: 2 }}>
        <CardContent>
          <Typography variant='h6'>Sample #3 - Nested Conditional</Typography>
          <ul>
            <Typography>(printf (cond [(cond [(&gt; 2 1) true]</Typography>
            <Typography>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[else false]) 1]
            </Typography>
            <Typography>&nbsp;&nbsp;&nbsp;&nbsp;[else 2]))</Typography>
          </ul>
        </CardContent>
      </Card>
    </Box>
  )
}
