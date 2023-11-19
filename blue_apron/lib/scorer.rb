class Scorer
  BEATS = { :p => :r, :r => :s, :s => :p }

  def evaluate_round(comp_decision, user_input)
    if comp_decision == user_input
      { winner: :tie, declaration: "It's a tie!" }
    elsif BEATS[comp_decision] == user_input
      { winner: :computer, declaration: "Computer wins!" }
    else
      { winner: :user, declaration: "You win!" }
    end
  end
end
