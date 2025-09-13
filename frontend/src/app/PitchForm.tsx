"use client";
import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { generatePitch } from "@/lib/api";

export default function PitchForm() {
  const [idea, setIdea] = useState("");
  const [pitch, setPitch] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPitch(null);
    try {
      const result = await generatePitch(idea);
      setPitch(result.pitch);
    } catch (err: any) {
      setError(err.message || "Error generating pitch");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card className="max-w-md mx-auto mt-8 p-6">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <Label htmlFor="idea">Your Product Idea</Label>
          <Input
            id="idea"
            value={idea}
            onChange={e => setIdea(e.target.value)}
            placeholder="Describe your idea..."
            required
          />
        </div>
        <Button type="submit" disabled={loading || !idea}>
          {loading ? "Generating..." : "Generate Pitch"}
        </Button>
      </form>
      {pitch && (
        <Card className="mt-6 bg-muted p-4">
          <strong>Pitch:</strong>
          <div className="mt-2">{pitch}</div>
        </Card>
      )}
      {error && (
        <div className="mt-4 text-red-500">{error}</div>
      )}
    </Card>
  );
}
