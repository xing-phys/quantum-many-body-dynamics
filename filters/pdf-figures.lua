-- Preserve vector originals in the combined PDF while using PNGs on the web.
function Image(img)
  if FORMAT:match('latex') and img.src:match('%.png$') then
    local vector = img.src:gsub('%.png$', '.pdf')
    local file = io.open(vector, 'rb')
    if file then file:close(); img.src = vector end
  end
  return img
end
