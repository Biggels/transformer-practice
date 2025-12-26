# Transformer Training Project - Learning Plan

## Project Goal
Train a small transformer model on a simple dataset (Shakespeare or BabyLM) to understand training dynamics and experiment with how different hyperparameters affect learning, grokking, and generalization vs. memorization.

## Learning Philosophy
- Build piece by piece, understanding each component before moving on
- Experiment and observe at each stage
- Learning takes priority over shipping - diversions to explore concepts are encouraged
- Work at the PyTorch layer: not raw matrix math, but building the architecture explicitly

## Stage 1: PyTorch Foundations
**Goal:** Get comfortable with tensors, shapes, and basic operations

- Create, reshape, and index tensors
- Understand batching and dimensions
- Practice thinking in shapes: (batch, sequence, features)
- Build intuition through hands-on experimentation, not visualization

## Stage 2: Data Preparation
**Goal:** Understand tokenization and how text becomes numbers

- Load a simple dataset (start with Shakespeare - single file, easy to work with)
- Implement or use a tokenizer
- Create sequences with context windows
- Understand how data is batched for training

## Stage 3: Transformer Components (Build Each, Then Experiment)
**Goal:** Implement each piece of the transformer and see what it does

### 3a. Embeddings + Positional Encoding
- Token embeddings: vocabulary → vectors
- Positional encoding: sine/cosine waves
- Experiment: what happens if you skip positional encoding?

### 3b. Attention Mechanism
- Query, Key, Value transformations
- Attention scores and softmax
- Masked attention (can't look ahead)
- Experiment: visualize attention patterns, try different numbers of heads

### 3c. Feed-Forward Network
- Simple MLP layer
- Understand where "world knowledge" lives
- Experiment: vary the size, see what breaks

### 3d. Full Transformer Block
- Put attention + FFN together with residual connections and layer norm
- Stack multiple blocks
- Experiment: how many blocks do we actually need for Shakespeare?

## Stage 4: Training Loop
**Goal:** Understand the training process end-to-end

- Forward pass: tokens → predictions
- Loss calculation: cross-entropy
- Backpropagation (PyTorch handles this, but understand what's happening)
- Optimizer step
- Experiment: watch loss curves, see when overfitting starts

## Stage 5: Experimentation & Grokking
**Goal:** This is where the real learning happens

Variables to play with:
- Learning rate
- Weight decay
- Model size (layers, dimensions, heads)
- Dataset size / repetition
- Training duration

Phenomena to observe:
- Grokking: sudden generalization after long training
- Memorization vs. generalization
- How different hyperparameters affect the quality and style of generated text

## Current Status
Stage 0: Planning and understanding baseline knowledge ✓
Next: Stage 1 - PyTorch Foundations

## Notes
- Using 6GB GPU - keep model small (probably <10M parameters)
- Primary interest: understanding training dynamics, not model performance
- It's okay if the model is "bad" - we're here to learn, not to ship
