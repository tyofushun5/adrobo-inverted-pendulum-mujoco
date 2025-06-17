import mujoco
from PIL import Image

xml = """
<mujoco>
  <worldbody>
    <light name="top" pos="0 0 1"/>
    <geom name="red_box" type="box" size=".2 .2 .2" rgba="1 0 0 1"/>
    <geom name="green_sphere" pos=".2 .2 .2" size=".1" rgba="0 1 0 1"/>
  </worldbody>
</mujoco>
"""
# ライトを適用したMJCFモデルの作成
model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)
renderer = mujoco.Renderer(model)

# 順動力学の適用 (data -> model)
mujoco.mj_forward(model, data)
# シーンを保持する MjvScene を更新する
renderer.update_scene(data)

# 画像の表示
Image.fromarray(renderer.render()).show()



