require 'spec_helper'

describe InputEvaluator do
  attr_reader :input_evaluator

  before :each do
    @input_evaluator = InputEvaluator.new
  end

  it "correctly evaluates correct input" do
    expect(input_evaluator.is_invalid?(:r)).to be false
    expect(input_evaluator.is_invalid?(:p)).to be false
    expect(input_evaluator.is_invalid?(:s)).to be false
  end

  it "correctly evaluates incorrect input" do
    expect(input_evaluator.is_invalid?("rock")).to be true
    expect(input_evaluator.is_invalid?(:fsafasdfs)).to be true
    expect(input_evaluator.is_invalid?("any string")).to be true
    expect(input_evaluator.is_invalid?("")).to be true
    expect(input_evaluator.is_invalid?(12345)).to be true
  end
end
