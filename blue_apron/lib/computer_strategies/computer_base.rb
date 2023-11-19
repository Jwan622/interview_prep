class ComputerBase
  BEATS = { r: :s, p: :r, s: :p }

  def play_gt_optimal
    [:p, :s, :r].sample
  end
end
