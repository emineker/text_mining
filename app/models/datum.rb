class Datum < ActiveRecord::Base
  attr_accessible :title, :content, :class_name, :file_name, :index_order

  validates_presence_of :content, :class_name, :file_name, :index_order
end
