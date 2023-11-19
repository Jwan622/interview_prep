class ScoreKeeper
  attr_reader :standings

  def initialize
    @standings = { user: 0, computer: 0, tie: 0 }
  end

  def increments(victor_and_declaration)
    standings[victor_and_declaration[:winner]] += 1
    standings
  end
end
