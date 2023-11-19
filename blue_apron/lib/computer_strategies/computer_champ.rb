require_relative 'computer_base'

class ComputerChamp < ComputerBase
  attr_reader :last_tally,
              :strategy_name

  def initialize
    @strategy_name = "champ"
    @last_tally = { r:0, s:0, p:0 }
  end

  def make_decision(tally)
    throw_difference = last_tally.merge(tally) {|key, old_throws, new_throws| new_throws - old_throws }
    @last_tally = tally.dup
    last_move = throw_difference.max_by { |key, throws| throws }[0]
    BEATS.key(last_move)
  end
end
