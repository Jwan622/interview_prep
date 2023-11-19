require 'spec_helper'

describe Scorer do
  attr_reader :scorer

  before :each do
    @scorer = Scorer.new
  end

  it "correctly picks a tie" do
    expect(scorer.evaluate_round(:r, :r)).to eql({ winner: :tie, declaration: "It's a tie!" })
    expect(scorer.evaluate_round(:s, :s)).to eql({ winner: :tie, declaration: "It's a tie!" })
    expect(scorer.evaluate_round(:p, :p)).to eql({ winner: :tie, declaration: "It's a tie!" })
  end

  it "correctly picks the computer if it wins" do
    expect(scorer.evaluate_round(:r, :s)).to eql({ winner: :computer, declaration: "Computer wins!" })
    expect(scorer.evaluate_round(:s, :p)).to eql({ winner: :computer, declaration: "Computer wins!" })
    expect(scorer.evaluate_round(:p, :r)).to eql({ winner: :computer, declaration: "Computer wins!" })
  end

  it "correctly picks the user if it wins" do
    expect(scorer.evaluate_round(:r, :p)).to eql({ winner: :user, declaration: "You win!" })
    expect(scorer.evaluate_round(:p, :s)).to eql({ winner: :user, declaration: "You win!" })
    expect(scorer.evaluate_round(:s, :r)).to eql({ winner: :user, declaration: "You win!" })
  end
end
