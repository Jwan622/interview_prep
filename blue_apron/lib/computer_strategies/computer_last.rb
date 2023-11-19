require_relative 'computer_base'

class ComputerLast < ComputerBase
  attr_reader :strategy_name,
              :last_tally,
              :second_to_last_move

  def initialize
    @strategy_name = "last move"
    @last_tally = { r:0, s:0, p:0 }
    @second_to_last_move = nil
  end

  def make_decision(tally)
    throw_difference = last_tally.merge(tally) {|key, old_throws, new_throws| new_throws - old_throws }
    @last_tally = tally.dup
    if second_to_last_move.nil?
      comp_move = play_gt_optimal
    else
      comp_move = BEATS.key(second_to_last_move)
    end
    @second_to_last_move = throw_difference.max_by { |key, throws| throws }[0]
    comp_move
  end
end
