class InputEvaluator
  VALID_CHOICES = [:r, :p, :s, :q]

  def is_invalid?(user_input)
    !VALID_CHOICES.include?(user_input)
  end
end
