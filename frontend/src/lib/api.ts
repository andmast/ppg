export async function generatePitch(idea: string) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000'}/api/v1/pitch`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ idea })
  });
  if (!res.ok) throw new Error('Failed to generate pitch');
  return res.json();
}
