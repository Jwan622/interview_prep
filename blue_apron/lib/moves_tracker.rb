class MovesTracker
  attr_reader :tally

  def initialize
    @tally = { r: 0, p:0, s:0 }
  end

  def update(decision)
    tally[decision.to_sym] += 1
  end
end
